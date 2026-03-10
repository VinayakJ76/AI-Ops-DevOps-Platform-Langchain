import os

provider = os.getenv("LLM_PROVIDER", "openai")


def analyze_incident(metrics, logs):

    if provider == "openai":

        from openai import OpenAI

        client = OpenAI(
            api_key=os.getenv("OPENAI_API_KEY")
        )

        prompt = f"""
        You are a Kubernetes SRE AI.

        Metrics:
        {metrics}

        Logs:
        {logs}

        Identify root cause and remediation.
        """

        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content


    elif provider == "anthropic":

        import anthropic

        client = anthropic.Anthropic(
            api_key=os.getenv("ANTHROPIC_API_KEY")
        )

        message = client.messages.create(
            model="claude-3-haiku-20240307",
            max_tokens=500,
            messages=[{
                "role": "user",
                "content": prompt
            }]
        )

        return message.content