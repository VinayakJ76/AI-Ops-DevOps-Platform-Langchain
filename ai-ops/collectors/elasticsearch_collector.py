import os
import requests


class ElasticsearchCollector:

    def __init__(self):

        self.url = os.getenv(
            "ELASTICSEARCH_URL",
            "http://elasticsearch.logging.svc.cluster.local:9200"
        )


    def collect(self):

        r = requests.get(
            f"{self.url}/_search",
            json={
                "size": 10,
                "query": {
                    "match": {
                        "level": "error"
                    }
                }
            }
        )

        return r.json()