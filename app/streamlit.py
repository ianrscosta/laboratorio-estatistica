import pandas as pd
import streamlit as st


data = pd.read_csv("./data/hour.csv")

st.title("Statistical Laboratory")
st.subheader("Bike Sharing Dataset")
st.dataframe(data.head(20), use_container_width=True)


selected_variable = st.selectbox(
    "Select a variable",
    options = data.columns.tolist(),
)

frequency_table = (
    data[selected_variable]
    .value_counts()
    .rename_axis("value")
    .reset_index(name="frequency")
)

st.dataframe(frequency_table)
