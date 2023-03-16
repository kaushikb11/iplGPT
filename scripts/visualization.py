from questions import QUESTIONS

from ipl_gpt.agents import default_sql_agent
from ipl_gpt.callbacks import get_data_callback

# Work in progress


db_path = "sqlite:///../ipl.sqlite"

agent_executor = default_sql_agent(db_path)


for question in QUESTIONS:
    with get_data_callback() as cb:
        response = agent_executor.run(question)
        print(f"Question : {question}")
        print(f"Answer : {response}")
        print(cb.data, cb.outputs)
