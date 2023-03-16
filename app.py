import os

import streamlit as st

from ipl_gpt.agents import default_sql_agent

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
    response = _agent.run(query_text)
    return str(response)


agent = get_sql_agent()

st.title("IPL GPT 🏏")

query = st.text_input("Ask any question about IPL", key="query")

if len(st.session_state.query) > 0:
    response = send_query_to_agent(agent, st.session_state.query)
    st.markdown(response)
