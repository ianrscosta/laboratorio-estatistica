from math import lgamma

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

import src.mystats as my

data = pd.read_csv("./data/hour.csv")

normal_distribution_variables = [
    "temp",
    "atemp",
    "hum",
    "windspeed",
]

poisson_distribution_variables = ["casual", "registered", "cnt"]

left, center_left, center_right, right = st.columns([0.7, 1, 1, 0.7])

with center_left:
    st.header("Normal curve")

    selected_population = st.selectbox(
        "Select a population",
        options=normal_distribution_variables,
    )

    normal_population = data[selected_population].dropna().tolist()

    population_mean = my.mean(*normal_population)
    population_deviation = my.std_deviation(*normal_population)

    x_values = np.linspace(
        min(normal_population),
        max(normal_population),
        300,
    )

    normal_density = (
        1
        / (population_deviation * np.sqrt(2 * np.pi))
        * np.exp(-0.5 * ((x_values - population_mean) / population_deviation) ** 2)
    )

    figure_normal, axis_normal = plt.subplots(figsize=(10, 7))

    axis_normal.hist(
        normal_population,
        bins=30,
        density=True,
        edgecolor="black",
        alpha=0.6,
        label="Observed data",
    )

    axis_normal.plot(
        x_values,
        normal_density,
        color="red",
        linewidth=2,
        label="Normal distribution",
    )

    axis_normal.set_title(f"{selected_population}: observed data and Normal curve")
    axis_normal.set_xlabel(selected_population)
    axis_normal.set_ylabel("Density")
    axis_normal.legend()

    st.pyplot(figure_normal)
    plt.close(figure_normal)

with center_right:
    st.header("Poisson distribution")

    selected_count = st.selectbox(
        "Select a count variable",
        options=poisson_distribution_variables,
    )

    poisson_population = data[selected_count].dropna().astype(int).tolist()

    poisson_mean = my.mean(*poisson_population)

    observed_values, observed_counts = np.unique(
        poisson_population,
        return_counts=True,
    )

    observed_percentage = observed_counts / len(poisson_population) * 100

    poisson_values = np.arange(
        min(observed_values),
        max(observed_values) + 1,
    )

    poisson_probabilities = np.array(
        [
            np.exp(k * np.log(poisson_mean) - poisson_mean - lgamma(k + 1))
            for k in poisson_values
        ]
    )

    poisson_percentage = poisson_probabilities * 100

    figure_poisson, axis_poisson = plt.subplots(figsize=(10, 7))

    axis_poisson.bar(
        observed_values,
        observed_percentage,
        alpha=0.6,
        label="Observed relative frequency",
    )

    axis_poisson.plot(
        poisson_values,
        poisson_percentage,
        color="red",
        marker="o",
        linewidth=2,
        label="Poisson distribution",
    )

    axis_poisson.set_title(f"{selected_count}: observed data and Poisson distribution")
    axis_poisson.set_xlabel("Rentals / hour")
    axis_poisson.set_ylabel("Probability (%)")
    axis_poisson.legend()

    st.pyplot(figure_poisson)
    plt.close(figure_poisson)

    st.write(
        "The data data doesn't fully match with the Poisson distribution,",
        "as Poisson expects repetitions at a constant rate,",
        "while the bike rentals vary by temperature, month, etc",
    )
