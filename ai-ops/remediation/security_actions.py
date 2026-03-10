import logging
import subprocess


def block_ip(context):
    """
    Block a suspicious IP address detected by the rule engine.

    Expected context keys:
        ip (str)        -> source IP to block
        reason (str)    -> reason for blocking
    """

    ip = context.get("ip")
    reason = context.get("reason", "security incident")

    if not ip:
        logging.warning("block_ip called but no IP provided in context")
        return

    logging.warning(f"Blocking IP {ip} due to {reason}")

    try:
        subprocess.run(
            ["iptables", "-A", "INPUT", "-s", ip, "-j", "DROP"],
            check=False
        )

    except Exception as e:
        logging.error(f"Failed to block IP {ip}: {e}")


def unblock_ip(context):
    """
    Remove a previously blocked IP.

    Expected context keys:
        ip (str)
    """

    ip = context.get("ip")

    if not ip:
        logging.warning("unblock_ip called but no IP provided in context")
        return

    logging.info(f"Removing block for IP {ip}")

    try:
        subprocess.run(
            ["iptables", "-D", "INPUT", "-s", ip, "-j", "DROP"],
            check=False
        )

    except Exception as e:
        logging.error(f"Failed to unblock IP {ip}: {e}")