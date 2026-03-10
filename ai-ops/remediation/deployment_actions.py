import subprocess


def restart_deployment(context):

    name = context.get("deployment")

    subprocess.run([
        "kubectl",
        "rollout",
        "restart",
        "deployment",
        name
    ])


def scale_deployment(context):

    name = context.get("deployment")

    replicas = context.get("replicas", 3)

    subprocess.run([
        "kubectl",
        "scale",
        "deployment",
        name,
        f"--replicas={replicas}"
    ])