from questions import QUESTIONS

from ipl_gpt.agents import default_csv_agent

csv_file = "../data/IPL_Matches_2008_2022.csv"

agent_executor = default_csv_agent(csv_file=csv_file)


for question in QUESTIONS:
    response = agent_executor.run(question)
    print(f"Question : {question}")
    print(f"Answer : {response}")
