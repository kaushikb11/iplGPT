from questions import QUESTIONS

from ipl_gpt.agents import default_sql_agent

db_path = "sqlite:///../ipl.sqlite"

agent_executor = default_sql_agent(db_path)


for question in QUESTIONS:
    response = agent_executor.run(question)
    print(f"Question : {question}")
    print(f"Answer : {response}")
