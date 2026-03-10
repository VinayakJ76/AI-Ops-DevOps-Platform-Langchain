import yaml
import os

from remediation.actions import ACTION_REGISTRY


class RuleEngine:

    def __init__(self):

        rules_dir = "knowledge"

        self.rules = []

        for file in os.listdir(rules_dir):

            if file.endswith(".yaml"):

                path = os.path.join(rules_dir, file)

                with open(path) as f:
                    data = yaml.safe_load(f)

                    if data and "issues" in data:
                        self.rules.extend(data["issues"])


    def evaluate(self, metrics, logs, cluster):

        for rule in self.rules:

            detection = rule["detection"]

            if detection in metrics:

                threshold = rule.get("threshold", 0)

                if metrics[detection] > threshold:
                    return rule

        return None


    def execute(self, rule):

        action = rule["action"]

        if action in ACTION_REGISTRY:

            ACTION_REGISTRY[action]({})