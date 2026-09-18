import streamlit as st
import pandas as pd

data = pd.read_csv("data/hour.csv")

st.title("Dataset")
st.dataframe(
    data,
    use_container_width = True,
    height = 700,
    hide_index = True,
)
