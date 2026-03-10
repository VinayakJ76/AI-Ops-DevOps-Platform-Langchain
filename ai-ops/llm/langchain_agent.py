from llm.llm_config import get_llm
from llm.prompt_templates import incident_prompt


class IncidentAnalyzer:

    def __init__(self):

        self.llm = get_llm()

        self.chain = incident_prompt | self.llm


    def analyze(self, metrics, logs, cluster):

        result = self.chain.invoke(
            {
                "metrics": metrics,
                "logs": logs,
                "cluster": cluster
            }
        )

        return result.content