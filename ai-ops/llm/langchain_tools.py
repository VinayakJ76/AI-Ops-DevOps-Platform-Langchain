from langchain.tools import tool


@tool
def get_metrics(metrics):
    """
    Returns system metrics from Prometheus.
    """
    return metrics


@tool
def get_logs(logs):
    """
    Returns recent application logs from Elasticsearch.
    """
    return logs


@tool
def get_cluster_state(cluster):
    """
    Returns Kubernetes cluster state.
    """
    return cluster