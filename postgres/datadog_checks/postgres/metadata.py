# (C) Datadog, Inc. 2021-present
# All rights reserved
# Licensed under a 3-clause BSD style license (see LICENSE)

from typing import Dict, Optional, Tuple  # noqa: F401

import time
import json
import psycopg2

try:
    import datadog_agent
except ImportError:
    from ..stubs import datadog_agent

from datadog_checks.base import is_affirmative
from datadog_checks.base.utils.db.utils import (
    DBMAsyncJob,
    RateLimitingTTLCache,
    default_json_event_encoding,
    obfuscate_sql_with_metadata,
)
from datadog_checks.postgres.connections import MultiDatabaseConnectionPool
from datadog_checks.base.utils.tracking import tracked_method

# default collection interval in minutes
DEFAULT_COLLECTION_INTERVAL = 30

PG_SETTINGS_QUERY = """
SELECT name, setting, category, short_desc FROM pg_settings
"""

def agent_check_getter(self):
    return self._check


class PostgresMetadata(DBMAsyncJob):
    """
    Collects statement samples and execution plans.
    """

    def __init__(self, check, config, shutdown_callback):
        collection_interval = float(
            config.metadata_config.get('collection_interval', DEFAULT_COLLECTION_INTERVAL)
        )
        if collection_interval <= 0:
            collection_interval = DEFAULT_COLLECTION_INTERVAL

        # convert collection interval from minutes to seconds
        collection_interval = collection_interval * 60

        self._conn_pool = MultiDatabaseConnectionPool(check._new_connection)

        def shutdown_cb():
            self._conn_pool.close_all_connections()
            return shutdown_callback()

        # TODO: check this stuff, not sure if its correct
        super(PostgresMetadata, self).__init__(
            check,
            rate_limit=1 / collection_interval,
            run_sync=is_affirmative(config.metadata_config.get('run_sync', False)),
            enabled=is_affirmative(config.metadata_config.get('enabled', False)),
            dbms="postgres",
            min_collection_interval=config.min_collection_interval,
            expected_db_exceptions=(psycopg2.errors.DatabaseError,),
            job_name="query-metadata",
            shutdown_callback=shutdown_cb,
        )
        self._check = check
        self._config = config
        self._conn_ttl_ms = self._config.idle_connection_timeout
        self._tags_no_db = None
        self.tags = None

    def _dbtags(self, db, *extra_tags):
        """
        Returns the default instance tags with the initial "db" tag replaced with the provided tag
        """
        t = ["db:" + db]
        if extra_tags:
            t.extend(extra_tags)
        if self._tags_no_db:
            t.extend(self._tags_no_db)
        return t

    def run_job(self):
        # do not emit any dd.internal metrics for DBM specific check code
        self.tags = [t for t in self._tags if not t.startswith('dd.internal')]
        self._tags_no_db = [t for t in self.tags if not t.startswith('db:')]
        self.report_postgres_settings()
        self._conn_pool.prune_connections()

    @tracked_method(agent_check_getter=agent_check_getter)
    def report_postgres_settings(self):
        rows = self._collect_postgres_settings()
        if rows:
            event = {
                "host": self._check.resolved_hostname,
                "agent_version": datadog_agent.get_version(),
                "dbms": "postgres",
                "kind": "pg_settings",
                "tags": self._tags_no_db,
                "timestamp": time.time() * 1000,
                "cloud_metadata": self._config.cloud_metadata,
                "metadata": rows,
            }
            self._check.database_monitoring_metadata(
                json.dumps(event, default=default_json_event_encoding)
            )

    @tracked_method(agent_check_getter=agent_check_getter)
    def _collect_postgres_settings(self):
        with self._conn_pool.get_connection(self._config.dbname, ttl_ms=self._conn_ttl_ms).cursor(
                cursor_factory=psycopg2.extras.DictCursor
        ) as cursor:
            self._log.debug("Running query [%s] %s", PG_SETTINGS_QUERY)
            cursor.execute(PG_SETTINGS_QUERY)
            rows = cursor.fetchall()
            self._log.debug("Loaded %s rows from pg_settings", len(rows))
            return [dict(row) for row in rows]

