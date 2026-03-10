import logging

from collectors.prometheus_collector import PrometheusCollector
from collectors.elasticsearch_collector import ElasticsearchCollector
from collectors.kubernetes_collector import KubernetesCollector

from agent.rule_engine import RuleEngine
from llm.langchain_agent import IncidentAnalyzer


logging.basicConfig(level=logging.INFO)

rule_engine = RuleEngine()
analyzer = IncidentAnalyzer()


def run_agent():

    logging.info("Starting AI Ops agent")

    prom = PrometheusCollector()
    es = ElasticsearchCollector()
    k8s = KubernetesCollector()

    metrics = prom.collect()
    logs = es.collect()
    cluster = k8s.collect()

    rule = rule_engine.evaluate(metrics, logs, cluster)

    if rule:
        logging.info(f"Known issue detected: {rule['name']}")
        rule_engine.execute(rule)

    else:
        logging.info("Unknown issue detected, invoking LangChain")

        result = analyzer.analyze(metrics, logs, cluster)

        logging.info("AI Analysis Result:")
        logging.info(result)


if __name__ == "__main__":
    run_agent()