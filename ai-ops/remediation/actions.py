from remediation.pod_actions import restart_pod
from remediation.deployment_actions import restart_deployment
from remediation.cleanup_actions import cleanup_container_logs
from remediation.security_actions import block_ip
from notifications.notifier import notify_engineer


ACTION_REGISTRY = {

    # Pod remediation
    "restart_pod": restart_pod,

    # Deployment remediation
    "restart_deployment": restart_deployment,

    # Cleanup remediation
    "cleanup_logs": cleanup_container_logs,

    # Security remediation
    "block_ip": block_ip,

    # Notifications
    "notify_engineer": notify_engineer
}