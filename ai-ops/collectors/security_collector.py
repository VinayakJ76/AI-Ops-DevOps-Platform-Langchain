import re


class SecurityCollector:

    def detect_bruteforce(self, logs):

        failed = {}

        for log in logs:

            if "login failed" in log["message"]:

                ip = log.get("source_ip")

                failed[ip] = failed.get(ip, 0) + 1

        return failed


    def detect_sql_injection(self, logs):

        patterns = ["' OR 1=1", "UNION SELECT", "DROP TABLE"]

        matches = []

        for log in logs:

            for p in patterns:

                if p.lower() in log["message"].lower():
                    matches.append(log)

        return matches