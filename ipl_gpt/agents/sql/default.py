import os

from langchain.agents import create_sql_agent
from langchain.agents.agent import AgentExecutor
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.llms.openai import OpenAI
from langchain.sql_database import SQLDatabase

# TODO: Remove it later
os.environ["OPENAI_API_KEY"] = "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"


def default_sql_agent(sqlite_url: str) -> AgentExecutor:
    db = SQLDatabase.from_uri(sqlite_url)
    toolkit = SQLDatabaseToolkit(db=db)
    return create_sql_agent(llm=OpenAI(temperature=0), toolkit=toolkit, verbose=True)
