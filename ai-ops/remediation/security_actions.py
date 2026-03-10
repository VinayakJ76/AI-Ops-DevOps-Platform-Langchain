import subprocess


def block_ip(context):

    ip = context.get("source_ip")

    if not ip:
        return

    cmd = [
        "iptables",
        "-A",
        "INPUT",
        "-s",
        ip,
        "-j",
        "DROP"
    ]

    subprocess.run(cmd)


def unblock_ip(context):

    ip = context.get("source_ip")

    cmd = [
        "iptables",
        "-D",
        "INPUT",
        "-s",
        ip,
        "-j",
        "DROP"
    ]

    subprocess.run(cmd)