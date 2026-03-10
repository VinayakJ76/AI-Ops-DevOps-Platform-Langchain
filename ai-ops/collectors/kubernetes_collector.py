from kubernetes import client, config

class KubernetesCollector:

    def __init__(self):
        config.load_incluster_config()
        self.v1 = client.CoreV1Api()

    def get_pods(self):
        return self.v1.list_pod_for_all_namespaces()

    def get_nodes(self):
        return self.v1.list_node()