import ast
import os

import pandas as pd
import streamlit as st

from ipl_gpt.agents import default_sql_agent
from ipl_gpt.callbacks import get_data_callback

st.set_page_config(
    page_title="IPL GPT",
    page_icon=":rocket:",
    # layout="wide",
    initial_sidebar_state="auto",
    menu_items={"Get help": "mailto:kaushikbokka@gmail.com"},
)


@st.cache_resource
def get_sql_agent():
    if not os.path.exists("ipl.sqlite"):
        raise FileNotFoundError(
            "ipl.sqlite not found. Use the `populate` script to create it."
        )
    return default_sql_agent("sqlite:///ipl.sqlite")


@st.cache_data(max_entries=200, persist=True, show_spinner=False)
def send_query_to_agent(_agent, query_text):
    with get_data_callback() as cb:
        response = _agent.run(query_text)
        return str(response), cb.data


agent = get_sql_agent()

st.title("IPL GPT 🏏")

query = st.text_input("Ask any question about IPL", key="query")

if len(st.session_state.query) > 0:
    response, data = send_query_to_agent(agent, st.session_state.query)
    st.markdown(response)
    data = ast.literal_eval(data)
    if len(data) > 1:
        values = [value[1] for value in data]
        indexes = [index[0] for index in data]
        data = pd.DataFrame(values, index=indexes, columns=["Count"])
        # data.reset_index(drop=True, inplace=True)
        if len(data) > 1:
            df, chart = st.columns(2)
            df.dataframe(data, use_container_width=True)
            chart.bar_chart(data)
