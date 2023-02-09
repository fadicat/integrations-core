# (C) Datadog, Inc. 2022-present
# All rights reserved
# Licensed under Simplified BSD License (see LICENSE)


LATENCY_METRICS = [
    'zookeeper.latency.min',
    'zookeeper.latency.avg',
    'zookeeper.latency.max',
]

STAT_METRICS = [
    'zookeeper.bytes_received',
    'zookeeper.bytes_sent',
    'zookeeper.connections',
    'zookeeper.connections',
    'zookeeper.outstanding_requests',
    'zookeeper.zxid.epoch',
    'zookeeper.zxid.count',
    'zookeeper.nodes',
    'zookeeper.instances',
    'zookeeper.packets.received',
    'zookeeper.packets.sent',
]


MNTR_METRICS = [
    'zookeeper.packets_sent',
    'zookeeper.approximate_data_size',
    'zookeeper.num_alive_connections',
    'zookeeper.open_file_descriptor_count',
    'zookeeper.avg_latency',
    'zookeeper.znode_count',
    'zookeeper.outstanding_requests',
    'zookeeper.min_latency',
    'zookeeper.ephemerals_count',
    'zookeeper.watch_count',
    'zookeeper.max_file_descriptor_count',
    'zookeeper.packets_received',
    'zookeeper.max_latency',
]

METRICS_34 = [*MNTR_METRICS, 'zookeeper.packets.sent', 'zookeeper.latency.avg', 'zookeeper.latency.min', 'zookeeper.connections', 'zookeeper.zxid.epoch', 'zookeeper.bytes_sent', 'zookeeper.bytes_received', 'zookeeper.instances', 'zookeeper.nodes', 'zookeeper.zxid.count', 'zookeeper.packets.received', 'zookeeper.latency.max']


METRICS_36 = [*METRICS_34, 'zookeeper.add_dead_watcher_stall_time', 'zookeeper.bytes_received_count', 'zookeeper.close_session_prep_time', 'zookeeper.close_session_prep_time_count', 'zookeeper.close_session_prep_time_sum', 'zookeeper.commit_commit_proc_req_queued', 'zookeeper.commit_commit_proc_req_queued_count', 'zookeeper.commit_commit_proc_req_queued_sum', 'zookeeper.commit_count', 'zookeeper.commit_process_time', 'zookeeper.commit_process_time_count', 'zookeeper.commit_process_time_sum', 'zookeeper.commit_propagation_latency', 'zookeeper.commit_propagation_latency_count', 'zookeeper.commit_propagation_latency_sum', 'zookeeper.concurrent_request_processing_in_commit_processor', 'zookeeper.concurrent_request_processing_in_commit_processor_count', 'zookeeper.concurrent_request_processing_in_commit_processor_sum', 'zookeeper.connection_drop_count', 'zookeeper.connection_drop_probability', 'zookeeper.connection_rejected', 'zookeeper.connection_request_count', 'zookeeper.connection_revalidate_count', 'zookeeper.connection_token_deficit', 'zookeeper.connection_token_deficit_count', 'zookeeper.connection_token_deficit_sum', 'zookeeper.dbinittime', 'zookeeper.dbinittime_count', 'zookeeper.dbinittime_sum', 'zookeeper.dead_watchers_cleaner_latency', 'zookeeper.dead_watchers_cleaner_latency_count', 'zookeeper.dead_watchers_cleaner_latency_sum', 'zookeeper.dead_watchers_cleared', 'zookeeper.dead_watchers_queued', 'zookeeper.diff_count', 'zookeeper.digest_mismatches_count', 'zookeeper.election_time', 'zookeeper.election_time_count', 'zookeeper.election_time_sum', 'zookeeper.ensemble_auth_fail', 'zookeeper.ensemble_auth_skip', 'zookeeper.ensemble_auth_success', 'zookeeper.follower_sync_time', 'zookeeper.follower_sync_time_count', 'zookeeper.follower_sync_time_sum', 'zookeeper.fsynctime', 'zookeeper.fsynctime_count', 'zookeeper.fsynctime_sum', 'zookeeper.global_sessions', 'zookeeper.inflight_diff_count_count', 'zookeeper.inflight_diff_count_sum', 'zookeeper.inflight_snap_count_count', 'zookeeper.inflight_snap_count_sum', 'zookeeper.jvm_buffer_pool_capacity_bytes', 'zookeeper.jvm_buffer_pool_used_buffers', 'zookeeper.jvm_buffer_pool_used_bytes', 'zookeeper.jvm_classes_loaded', 'zookeeper.jvm_classes_loaded_total', 'zookeeper.jvm_classes_unloaded_total', 'zookeeper.jvm_gc_collection_seconds_count', 'zookeeper.jvm_gc_collection_seconds_sum', 'zookeeper.jvm_info', 'zookeeper.jvm_memory_bytes_committed', 'zookeeper.jvm_memory_bytes_init', 'zookeeper.jvm_memory_bytes_max', 'zookeeper.jvm_memory_bytes_used', 'zookeeper.jvm_memory_pool_bytes_committed', 'zookeeper.jvm_memory_pool_bytes_init', 'zookeeper.jvm_memory_pool_bytes_max', 'zookeeper.jvm_memory_pool_bytes_used', 'zookeeper.jvm_pause_time_ms_count', 'zookeeper.jvm_pause_time_ms_sum', 'zookeeper.jvm_threads_current', 'zookeeper.jvm_threads_daemon', 'zookeeper.jvm_threads_deadlocked', 'zookeeper.jvm_threads_deadlocked_monitor', 'zookeeper.jvm_threads_peak', 'zookeeper.jvm_threads_started_total', 'zookeeper.jvm_threads_state', 'zookeeper.large_requests_rejected', 'zookeeper.last_client_response_size', 'zookeeper.learner_commit_received_count', 'zookeeper.learner_proposal_received_count', 'zookeeper.local_sessions', 'zookeeper.local_write_committed_time_ms', 'zookeeper.local_write_committed_time_ms_count', 'zookeeper.local_write_committed_time_ms_sum', 'zookeeper.looking_count', 'zookeeper.max_client_response_size', 'zookeeper.min_client_response_size', 'zookeeper.netty_queued_buffer_capacity', 'zookeeper.netty_queued_buffer_capacity_count', 'zookeeper.netty_queued_buffer_capacity_sum', 'zookeeper.node_changed_watch_count', 'zookeeper.node_changed_watch_count_count', 'zookeeper.node_changed_watch_count_sum', 'zookeeper.node_children_watch_count', 'zookeeper.node_children_watch_count_count', 'zookeeper.node_children_watch_count_sum', 'zookeeper.node_created_watch_count', 'zookeeper.node_created_watch_count_count', 'zookeeper.node_created_watch_count_sum', 'zookeeper.node_deleted_watch_count', 'zookeeper.node_deleted_watch_count_count', 'zookeeper.node_deleted_watch_count_sum', 'zookeeper.om_commit_process_time_ms', 'zookeeper.om_commit_process_time_ms_count', 'zookeeper.om_commit_process_time_ms_sum', 'zookeeper.om_proposal_process_time_ms', 'zookeeper.om_proposal_process_time_ms_count', 'zookeeper.om_proposal_process_time_ms_sum', 'zookeeper.outstanding_changes_queued', 'zookeeper.outstanding_changes_removed', 'zookeeper.outstanding_tls_handshake', 'zookeeper.pending_session_queue_size', 'zookeeper.pending_session_queue_size_count', 'zookeeper.pending_session_queue_size_sum', 'zookeeper.prep_process_time', 'zookeeper.prep_process_time_count', 'zookeeper.prep_process_time_sum', 'zookeeper.prep_processor_queue_size', 'zookeeper.prep_processor_queue_size_count', 'zookeeper.prep_processor_queue_size_sum', 'zookeeper.prep_processor_queue_time_ms', 'zookeeper.prep_processor_queue_time_ms_count', 'zookeeper.prep_processor_queue_time_ms_sum', 'zookeeper.prep_processor_request_queued', 'zookeeper.process_cpu_seconds_total', 'zookeeper.process_max_fds', 'zookeeper.process_open_fds', 'zookeeper.process_resident_memory_bytes', 'zookeeper.process_start_time_seconds', 'zookeeper.process_virtual_memory_bytes', 'zookeeper.propagation_latency', 'zookeeper.propagation_latency_count', 'zookeeper.propagation_latency_sum', 'zookeeper.proposal_ack_creation_latency', 'zookeeper.proposal_ack_creation_latency_count', 'zookeeper.proposal_ack_creation_latency_sum', 'zookeeper.proposal_count', 'zookeeper.proposal_latency', 'zookeeper.proposal_latency_count', 'zookeeper.proposal_latency_sum', 'zookeeper.quit_leading_due_to_disloyal_voter', 'zookeeper.quorum_ack_latency', 'zookeeper.quorum_ack_latency_count', 'zookeeper.quorum_ack_latency_sum', 'zookeeper.read_commit_proc_issued', 'zookeeper.read_commit_proc_issued_count', 'zookeeper.read_commit_proc_issued_sum', 'zookeeper.read_commit_proc_req_queued', 'zookeeper.read_commit_proc_req_queued_count', 'zookeeper.read_commit_proc_req_queued_sum', 'zookeeper.read_commitproc_time_ms', 'zookeeper.read_commitproc_time_ms_count', 'zookeeper.read_commitproc_time_ms_sum', 'zookeeper.read_final_proc_time_ms', 'zookeeper.read_final_proc_time_ms_count', 'zookeeper.read_final_proc_time_ms_sum', 'zookeeper.readlatency', 'zookeeper.readlatency_count', 'zookeeper.readlatency_sum', 'zookeeper.reads_after_write_in_session_queue', 'zookeeper.reads_after_write_in_session_queue_count', 'zookeeper.reads_after_write_in_session_queue_sum', 'zookeeper.reads_issued_from_session_queue', 'zookeeper.reads_issued_from_session_queue_count', 'zookeeper.reads_issued_from_session_queue_sum', 'zookeeper.request_commit_queued', 'zookeeper.request_throttle_wait_count', 'zookeeper.requests_in_session_queue', 'zookeeper.requests_in_session_queue_count', 'zookeeper.requests_in_session_queue_sum', 'zookeeper.response_packet_cache_hits', 'zookeeper.response_packet_cache_misses', 'zookeeper.response_packet_get_children_cache_hits', 'zookeeper.response_packet_get_children_cache_misses', 'zookeeper.revalidate_count', 'zookeeper.server_write_committed_time_ms', 'zookeeper.server_write_committed_time_ms_count', 'zookeeper.server_write_committed_time_ms_sum', 'zookeeper.session_queues_drained', 'zookeeper.session_queues_drained_count', 'zookeeper.session_queues_drained_sum', 'zookeeper.sessionless_connections_expired', 'zookeeper.snap_count', 'zookeeper.snapshottime', 'zookeeper.snapshottime_count', 'zookeeper.snapshottime_sum', 'zookeeper.stale_replies', 'zookeeper.stale_requests', 'zookeeper.stale_requests_dropped', 'zookeeper.stale_sessions_expired', 'zookeeper.startup_snap_load_time', 'zookeeper.startup_snap_load_time_count', 'zookeeper.startup_snap_load_time_sum', 'zookeeper.startup_txns_load_time', 'zookeeper.startup_txns_load_time_count', 'zookeeper.startup_txns_load_time_sum', 'zookeeper.startup_txns_loaded', 'zookeeper.startup_txns_loaded_count', 'zookeeper.startup_txns_loaded_sum', 'zookeeper.sync_process_time', 'zookeeper.sync_process_time_count', 'zookeeper.sync_process_time_sum', 'zookeeper.sync_processor_batch_size', 'zookeeper.sync_processor_batch_size_count', 'zookeeper.sync_processor_batch_size_sum', 'zookeeper.sync_processor_queue_and_flush_time_ms', 'zookeeper.sync_processor_queue_and_flush_time_ms_count', 'zookeeper.sync_processor_queue_and_flush_time_ms_sum', 'zookeeper.sync_processor_queue_flush_time_ms', 'zookeeper.sync_processor_queue_flush_time_ms_count', 'zookeeper.sync_processor_queue_flush_time_ms_sum', 'zookeeper.sync_processor_queue_size', 'zookeeper.sync_processor_queue_size_count', 'zookeeper.sync_processor_queue_size_sum', 'zookeeper.sync_processor_queue_time_ms', 'zookeeper.sync_processor_queue_time_ms_count', 'zookeeper.sync_processor_queue_time_ms_sum', 'zookeeper.sync_processor_request_queued', 'zookeeper.time_waiting_empty_pool_in_commit_processor_read_ms', 'zookeeper.time_waiting_empty_pool_in_commit_processor_read_ms_count', 'zookeeper.time_waiting_empty_pool_in_commit_processor_read_ms_sum', 'zookeeper.tls_handshake_exceeded', 'zookeeper.unrecoverable_error_count', 'zookeeper.updatelatency', 'zookeeper.updatelatency_count', 'zookeeper.updatelatency_sum', 'zookeeper.uptime', 'zookeeper.write_batch_time_in_commit_processor', 'zookeeper.write_batch_time_in_commit_processor_count', 'zookeeper.write_batch_time_in_commit_processor_sum', 'zookeeper.write_commit_proc_issued', 'zookeeper.write_commit_proc_issued_count', 'zookeeper.write_commit_proc_issued_sum', 'zookeeper.write_commit_proc_req_queued', 'zookeeper.write_commit_proc_req_queued_count', 'zookeeper.write_commit_proc_req_queued_sum', 'zookeeper.write_commitproc_time_ms', 'zookeeper.write_commitproc_time_ms_count', 'zookeeper.write_commitproc_time_ms_sum', 'zookeeper.write_final_proc_time_ms', 'zookeeper.write_final_proc_time_ms_count', 'zookeeper.write_final_proc_time_ms_sum']

METRICS_36_OPTIONAL = ['zookeeper.jvm_memory_pool_allocated_bytes_total']


# these metrics will report with `NaN` values, so we skip them
METRICS_36_E2E_SKIPS = [
    'zookeeper.close_session_prep_time',
    'zookeeper.commit_commit_proc_req_queued',
    'zookeeper.commit_process_time',
    'zookeeper.commit_propagation_latency',
    'zookeeper.concurrent_request_processing_in_commit_processor',
    'zookeeper.connection_token_deficit',
    'zookeeper.dead_watchers_cleaner_latency',
    'zookeeper.election_time',
    'zookeeper.follower_sync_time',
    'zookeeper.fsynctime',
    'zookeeper.local_write_committed_time_ms',
    'zookeeper.netty_queued_buffer_capacity',
    'zookeeper.node_changed_watch_count',
    'zookeeper.node_children_watch_count',
    'zookeeper.node_created_watch_count',
    'zookeeper.node_deleted_watch_count',
    'zookeeper.om_commit_process_time_ms',
    'zookeeper.om_proposal_process_time_ms',
    'zookeeper.pending_session_queue_size',
    'zookeeper.prep_process_time',
    'zookeeper.prep_processor_queue_time_ms',
    'zookeeper.propagation_latency',
    'zookeeper.proposal_ack_creation_latency',
    'zookeeper.proposal_latency',
    'zookeeper.quorum_ack_latency',
    'zookeeper.read_commit_proc_issued',
    'zookeeper.read_commit_proc_req_queued',
    'zookeeper.read_commitproc_time_ms',
    'zookeeper.read_final_proc_time_ms',
    'zookeeper.readlatency',
    'zookeeper.reads_after_write_in_session_queue',
    'zookeeper.reads_issued_from_session_queue',
    'zookeeper.requests_in_session_queue',
    'zookeeper.server_write_committed_time_ms',
    'zookeeper.session_queues_drained',
    'zookeeper.startup_txns_load_time',
    'zookeeper.startup_txns_loaded',
    'zookeeper.sync_process_time',
    'zookeeper.sync_processor_batch_size',
    'zookeeper.sync_processor_queue_and_flush_time_ms',
    'zookeeper.sync_processor_queue_flush_time_ms',
    'zookeeper.sync_processor_queue_time_ms',
    'zookeeper.time_waiting_empty_pool_in_commit_processor_read_ms',
    'zookeeper.updatelatency',
    'zookeeper.write_batch_time_in_commit_processor',
    'zookeeper.write_commit_proc_issued',
    'zookeeper.write_commit_proc_req_queued',
    'zookeeper.write_commitproc_time_ms',
    'zookeeper.write_final_proc_time_ms',
]
