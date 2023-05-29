from langchain.agents import create_csv_agent
from langchain.agents.agent import AgentExecutor
from langchain.llms.openai import OpenAI


def default_csv_agent(csv_file: str) -> AgentExecutor:
    return create_csv_agent(
        llm=OpenAI(temperature=0),
        path=csv_file,
        verbose=True,
    )
