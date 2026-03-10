import requests
import os


class PrometheusCollector:

    def __init__(self):

        self.url = os.getenv(
            "PROMETHEUS_URL",
            "http://prometheus.monitoring.svc.cluster.local:9090"
        )


    def collect(self):

        query = "up"

        r = requests.get(
            f"{self.url}/api/v1/query",
            params={"query": query}
        )

        data = r.json()

        return {
            "up": len(data.get("data", {}).get("result", []))
        }