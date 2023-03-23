import ast

import pandas as pd
import requests
import streamlit as st

st.set_page_config(
    page_title="IPL GPT",
    page_icon=":rocket:",
    # layout="wide",
    initial_sidebar_state="auto",
    menu_items={"Get help": "mailto:kaushikbokka@gmail.com"},
)


@st.cache_data(max_entries=200, persist=True, show_spinner=False)
def send_query_to_agent(query_text: str):
    params = {
        "search_query": st.session_state.query,
    }
    response = requests.post(
        "https://kaushikb11--ipl-gpt-fastapi-app.modal.run/search",
        params=params,
        headers=headers,
    )
    response = response.json()
    return response


st.title("IPL GPT 🏏")

headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
}

query = st.text_input("Ask any question about IPL", key="query")


def button_click(query):
    st.session_state.query = query


QUESTIONS = [
    "Top 5 players with the most Player of the Match awards?",
    "Which team won the maximum number of matches in IPL 2020?",
    "What's the number of runs scored by AB de Villiers season wise?",
]

for question in QUESTIONS:
    st.button(
        question,
        on_click=button_click,
        args=(question,),
        use_container_width=True,
        type="primary",
    )

if len(st.session_state.query) > 0:
    with st.spinner(text="In progress..."):
        response = send_query_to_agent(st.session_state.query)

        st.markdown(response["answer"])
        if response["tool_used"] == "Statistical Question Answering":
            data = ast.literal_eval(response["data"])
            if len(data) > 1:
                values = [value[1] for value in data]
                indexes = [index[0] for index in data]
                data = pd.DataFrame(values, index=indexes, columns=["Count"])
                # data.reset_index(drop=True, inplace=True)
                if len(data) > 1:
                    df, chart = st.columns(2)
                    df.dataframe(data, use_container_width=True)
                    chart.bar_chart(data)
