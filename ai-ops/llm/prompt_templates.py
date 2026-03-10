from langchain.prompts import PromptTemplate


incident_prompt = PromptTemplate(
    input_variables=["metrics", "logs", "cluster"],
    template="""
You are a Kubernetes Site Reliability Engineer.

Analyze the following data.

Metrics:
{metrics}

Logs:
{logs}

Cluster State:
{cluster}

Determine:

1. Root cause
2. Recommended remediation
3. Severity level
"""
)