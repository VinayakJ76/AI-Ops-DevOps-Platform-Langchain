import os
from langchain_openai import ChatOpenAI


def get_llm():

    model = os.getenv("LLM_MODEL", "gpt-4o-mini")

    llm = ChatOpenAI(
        model=model,
        temperature=0
    )

    return llm