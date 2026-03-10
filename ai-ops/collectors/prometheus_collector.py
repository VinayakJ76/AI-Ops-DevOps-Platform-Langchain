import requests

class PrometheusCollector:

    def __init__(self, url):
        self.url = url

    def query(self, q):
        r = requests.get(
            f"{self.url}/api/v1/query",
            params={"query": q},
            timeout=5
        )
        return r.json()

    def get_node_cpu(self):
        query = '100 - (avg by(instance)(rate(node_cpu_seconds_total{mode="idle"}[5m])) * 100)'
        return self.query(query)

    def get_disk_usage(self):
        query = 'node_filesystem_avail_bytes'
        return self.query(query)