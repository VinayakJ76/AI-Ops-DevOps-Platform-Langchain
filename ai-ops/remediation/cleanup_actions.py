import subprocess
import shutil
import os


def cleanup_docker_images():
    """
    Remove unused docker images
    """

    cmd = ["docker", "image", "prune", "-af"]

    subprocess.run(cmd, check=False)


def cleanup_docker_volumes():
    """
    Remove unused docker volumes
    """

    cmd = ["docker", "volume", "prune", "-f"]

    subprocess.run(cmd, check=False)


def cleanup_container_logs(log_dir="/var/log/containers"):
    """
    Remove old container logs
    """

    if not os.path.exists(log_dir):
        return

    for file in os.listdir(log_dir):

        path = os.path.join(log_dir, file)

        try:
            if os.path.isfile(path):
                os.remove(path)
        except Exception:
            pass


def cleanup_system_logs():
    """
    Cleanup journal logs
    """

    cmd = [
        "journalctl",
        "--vacuum-time=2d"
    ]

    subprocess.run(cmd, check=False)


def cleanup_tmp():
    """
    Cleanup /tmp directory
    """

    tmp_dir = "/tmp"

    for file in os.listdir(tmp_dir):

        path = os.path.join(tmp_dir, file)

        try:
            if os.path.isfile(path):
                os.remove(path)

            elif os.path.isdir(path):
                shutil.rmtree(path)

        except Exception:
            pass


def disk_usage():
    """
    Check disk usage
    """

    total, used, free = shutil.disk_usage("/")

    usage_percent = (used / total) * 100

    return usage_percent