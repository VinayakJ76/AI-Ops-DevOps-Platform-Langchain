import os

from langchain_openai import ChatOpenAI
from langchain.agents import initialize_agent
from langchain.agents import AgentType

from llm.langchain_tools import (
    get_metrics,
    get_logs,
    get_cluster_state
)

from llm.prompt_templates import INCIDENT_ANALYSIS_PROMPT


class IncidentAnalyzer:

    def __init__(self):

        self.llm = ChatOpenAI(
            model="gpt-4o-mini",
            temperature=0
        )

        self.tools = [
            get_metrics,
            get_logs,
            get_cluster_state
        ]

        self.agent = initialize_agent(
            tools=self.tools,
            llm=self.llm,
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            verbose=True
        )


    def analyze(self, metrics, logs, cluster):

        prompt = INCIDENT_ANALYSIS_PROMPT.format(
            metrics=metrics,
            logs=logs,
            cluster=cluster
        )

        result = self.agent.run(prompt)

        return result