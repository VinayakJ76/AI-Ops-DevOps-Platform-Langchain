import yaml

from collectors.prometheus_collector import PrometheusCollector
from collectors.elasticsearch_collector import ElasticsearchCollector
from collectors.kubernetes_collector import KubernetesCollector

from agent.decision_engine import handle_crashloop
from agent.scheduler import run_forever


def monitor():

    config = yaml.safe_load(open("/app/config/config.yaml"))

    prom = PrometheusCollector(config["prometheus_url"])
    es = ElasticsearchCollector(config["elasticsearch_url"])
    k8s = KubernetesCollector()

    pods = k8s.get_pods()

    handle_crashloop(pods)

    errors = es.search_errors()

    print("log errors:", errors)


if __name__ == "__main__":

    run_forever(monitor, 30)