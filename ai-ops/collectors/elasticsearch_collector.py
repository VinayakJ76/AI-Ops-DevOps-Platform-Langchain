import requests

class ElasticsearchCollector:

    def __init__(self, url):
        self.url = url

    def search_errors(self):

        query = {
          "query": {
            "match": {
              "log.level": "error"
            }
          }
        }

        r = requests.get(
            f"{self.url}/_search",
            json=query,
            timeout=5
        )

        return r.json()