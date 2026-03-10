import yaml
import os

from remediation.actions import ACTION_REGISTRY


class RuleEngine:

    def __init__(self, rules_dir):

        self.rules = []

        for file in os.listdir(rules_dir):

            if file.endswith(".yaml"):

                path = os.path.join(rules_dir, file)

                with open(path) as f:
                    data = yaml.safe_load(f)

                    if data and "issues" in data:
                        self.rules.extend(data["issues"])


    def evaluate(self, context):

        for rule in self.rules:

            detection = rule["detection"]

            if detection in context:

                value = context[detection]

                threshold = rule.get("threshold")

                triggered = False

                if threshold is None:
                    triggered = value

                else:
                    triggered = value > threshold

                if triggered:

                    action = rule["action"]

                    if action in ACTION_REGISTRY:

                        ACTION_REGISTRY[action](context)

                    else:

                        print("Unknown action:", action)