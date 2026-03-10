from llm.langchain_agent import IncidentAnalyzer


analyzer = IncidentAnalyzer()


def analyze_unknown_incident(metrics, logs, cluster):

    result = analyzer.analyze(metrics, logs, cluster)

    print("AI Incident Analysis:")
    print(result)

    return result