from kubernetes import client, config

config.load_incluster_config()

v1 = client.CoreV1Api()

def restart_pod(namespace, pod_name):

    v1.delete_namespaced_pod(
        name=pod_name,
        namespace=namespace
    )