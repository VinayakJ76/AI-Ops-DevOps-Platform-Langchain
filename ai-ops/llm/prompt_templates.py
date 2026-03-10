INCIDENT_ANALYSIS_PROMPT = """
You are an expert Kubernetes SRE.

Analyze the following system information and determine
the most likely root cause and remediation.

Metrics:
{metrics}

Logs:
{logs}

Cluster State:
{cluster}

Return:
1. Root cause
2. Recommended remediation
3. Severity
"""