from kubernetes import client, config


class KubernetesCollector:

    def __init__(self):

        try:
            config.load_incluster_config()
        except:
            config.load_kube_config()

        self.v1 = client.CoreV1Api()


    def collect(self):

        pods = self.v1.list_pod_for_all_namespaces()

        return {
            "pod_count": len(pods.items)
        }