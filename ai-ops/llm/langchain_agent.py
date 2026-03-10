import os

from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate


class IncidentAnalyzer:

    def __init__(self):

        self.llm = ChatOpenAI(
            model=os.getenv("LLM_MODEL", "gpt-4o-mini"),
            temperature=0
        )

        self.prompt = PromptTemplate(
            input_variables=["metrics", "logs", "cluster"],
            template="""
You are a Kubernetes SRE.

Metrics:
{metrics}

Logs:
{logs}

Cluster:
{cluster}

Explain root cause and recommended remediation.
"""
        )


    def analyze(self, metrics, logs, cluster):

        chain = self.prompt | self.llm

        result = chain.invoke(
            {
                "metrics": metrics,
                "logs": logs,
                "cluster": cluster
            }
        )

        return result.content