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

st.title("IPL GPT 🏏")

headers = {
    "accept": "application/json",
    "content-type": "application/x-www-form-urlencoded",
}

query = st.text_input("Ask any question about IPL", key="query")

if len(st.session_state.query) > 0:
    params = {
        "search_query": st.session_state.query,
    }
    response = requests.post(
        "https://kaushikb11--ipl-gpt-fastapi-app.modal.run/search",
        params=params,
        headers=headers,
    )
    # response, data = send_query_to_agent(agent, st.session_state.query)
    response = response.json()
    result = response["result"]
    data = response["data"]

    st.markdown(result)
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
