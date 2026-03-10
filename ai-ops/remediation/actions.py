from remediation.pod_actions import restart_pod
from remediation.cleanup_actions import cleanup_container_logs
from remediation.deployment_actions import restart_deployment, scale_deployment
from remediation.security_actions import block_ip
from notifications.notifier import notify_engineer


ACTION_REGISTRY = {

    "restart_pod": restart_pod,
    "restart_deployment": restart_deployment,
    "scale_deployment": scale_deployment,

    "cleanup_logs": cleanup_container_logs,

    "block_ip": block_ip,

    "notify_engineer": notify_engineer
}