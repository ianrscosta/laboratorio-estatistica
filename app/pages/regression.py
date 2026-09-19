import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

import src.mystats as my

st.title("Correlation and Regression")

data = pd.read_csv("./data/hour.csv")

numeric_data = [
    "temp",
    "atemp",
    "hum",
    "windspeed",
    "casual",
    "registered",
    "cnt",
]
left, center_left, center_right, right = st.columns([1, 1, 1, 1])

with center_left:
    first_variable = st.selectbox(
        "Select first variable",
        options=numeric_data,
    )

with center_right:
    second_variable = st.selectbox(
        "Select second variable",
        options=numeric_data,
    )

    selected_data = data[[first_variable, second_variable]].dropna()

    first_data = selected_data.iloc[:, 0].tolist()
    second_data = selected_data.iloc[:, 1].tolist()

left, center, right = st.columns([1, 2, 1])

with center:
    correlation = my.pearson_correlation(first_data, second_data)

    st.warning("Correlation doesn't imply causation")
    st.subheader(f"correlation = {correlation}")

    slope = my.covariance(first_data, second_data) / my.std_variance(*first_data)
    first_mean = my.mean(*first_data)
    second_mean = my.mean(*second_data)
    intercept = second_mean - slope * first_mean
    r_squared = correlation**2

    line_x = np.linspace(
        min(first_data),
        max(first_data),
        200,
    )

    line_y = [intercept + slope * x for x in line_x]

    figure, axis = plt.subplots()
    axis.set_title("Scatter")
    axis.scatter(
        first_data,
        second_data,
    )
    axis.plot(
        line_x,
        line_y,
        color="red",
        linewidth="2",
        label="Regression Line",
    )
    axis.set_xlabel(first_variable)
    axis.set_ylabel(second_variable)

    st.pyplot(figure)
    plt.close(figure)

    left, right = st.columns([1, 1], gap="large")

    with left:
        st.subheader("Regression results")

        st.write(
            f"Equation: ŷ = {intercept:.4f} ",
            f"+ ({slope:.4f} * {first_variable})",
        )
        st.write(f"R squared = {r_squared:.4f}")

        prediction_x = st.number_input(
            f"Enter a value for {first_variable}",
            min_value=float(min(first_data)),
            max_value=float(max(first_data)),
            value=float(my.mean(*first_data)),
        )

        prediction_y = intercept + slope * prediction_x

        st.metric(
            f"Prediction of {second_variable} is",
            f"{prediction_y:.4f}",
        )

    with right:
        st.subheader("Text prediction")

        if slope > 0:
            st.write(
                f"adding 1 to {first_variable}, increments {second_variable} in {slope:.4f}"
            )
        elif slope < 0:
            st.write(
                f"adding 1 to {first_variable}, decrements {second_variable} in {slope:.4f}"
            )
        else:
            st.write(f"adding 1 to {first_variable}, doesn't change {second_variable}")

        st.subheader("Intercept")
        st.write(f"Intercept = {intercept}")
        st.write(f"When {first_variable} = 0, {second_variable} = intercept")
