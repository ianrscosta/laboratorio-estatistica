import streamlit as st

dashboard = st.Page(
    "pages/dashboard.py",
    title="Dashboard",
)

dataset = st.Page(
    "pages/dataset.py",
    title="Data Set",
)

simulation = st.Page(
    "pages/simulation.py",
    title="Simulation",
)

distribution = st.Page(
    "pages/distribution.py",
    title="Distribution",
)

regression = st.Page(
    "pages/regression.py",
    title="Correlation and regression",
)

navigation = st.navigation(
    [dashboard, dataset, simulation, distribution, regression],
    position="top",
)

st.set_page_config(
    layout="wide",
)

navigation.run()
