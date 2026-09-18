import streamlit as st

dashboard = st.Page(
    "pages/dashboard.py",
    title = "Dashboard",
)

dataset = st.Page(
    "pages/dataset.py",
    title = "Data Set",
)

simulation = st.Page(
    "pages/simulation.py",
    title = "Simulation",
)

navigation = st.navigation(
    [dashboard, dataset, simulation],
    position = "top",
)

st.set_page_config(
    layout = "wide",
)

navigation.run()
