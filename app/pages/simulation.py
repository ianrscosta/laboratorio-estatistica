import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import streamlit as st

import src.mystats as my

numeric_data = [
    "temp",
    "atemp",
    "hum",
    "windspeed",
    "casual",
    "registered",
    "cnt",
]

left, center, right = st.columns([1, 2.5, 1])
data = pd.read_csv("./data/hour.csv")

with center:
    st.header("Law of Large Numbers")

    left, right = st.columns([1, 1])

    with left:
        selected_simulation = st.selectbox(
            "Select a simulation",
            options=["coin", "dice"],
        )

    with right:
        simulated_tosses = st.slider(
            "number of tosses",
            min_value=0.0,
            max_value=100000.0,
            value=0.0,
            step=1.0,
        )

    if selected_simulation == "coin":
        st.subheader("coin")

        results = []
        for number in range(int(simulated_tosses)):
            toss_result = np.random.default_rng().integers(0, 2)

            if toss_result == 1:
                results.append(1)
            elif toss_result == 0:
                results.append(0)

        heads = np.count_nonzero(np.array(results) == 0)
        tails = np.count_nonzero(np.array(results) == 1)

        heads_so_far = np.cumsum(np.array(results) == 0)
        relative_frequency = heads_so_far / np.arange(1, len(results) + 1)

        st.subheader("Results")

        left, right = st.columns([1, 1])
        with right:
            figure, axis = plt.subplots(figsize=(10, 5.4))
            axis.set_title("Results")
            axis.bar(
                ["Heads", "Tails"],
                [heads, tails],
            )
            axis.set_ylabel("frequency")
            st.pyplot(figure)
            plt.close(figure)

        with left:
            figure, axis = plt.subplots(figsize=(10, 5))
            axis.set_title("Relative frequency of heads")
            axis.plot(np.arange(1, len(results) + 1), relative_frequency)
            axis.axhline(
                0.5,
                color="red",
                linestyle="--",
            )
            axis.set_xlabel("number of tosses")
            axis.set_ylabel("relative frequency")
            axis.set_ylim(0, 1)
            st.pyplot(figure)
            plt.close(figure)

    elif selected_simulation == "dice":
        st.subheader("dice")
        st.subheader("Not implemented yet")

    st.header("Central Limit Theorem")

    right, center, left = st.columns([1, 1, 1])

    with left:
        selected_population = st.selectbox(
            "Select a population",
            options=numeric_data,
        )

    population = data[selected_population].dropna().tolist()

    with center:
        sample_size = st.slider(
            "Size of sample",
            min_value=1,
            max_value=len(population),
            value=30,
            step=1,
        )
    with right:
        sample_quantity = st.slider(
            "Number of samples",
            min_value=10,
            max_value=10000,
            value=1000,
            step=10,
        )

    sample_means = []
    for _ in range(sample_quantity):
        sample = np.random.default_rng().choice(
            population,
            size=sample_size,
            replace=True,
        )

        sample_means.append(my.mean(*sample))

    left, right = st.columns([1, 1])

    with left:
        figure, axis = plt.subplots(figsize=(10, 5))
        axis.hist(sample_means, bins=30, edgecolor="black")

        axis.set_title(f"Sampling distribution of {selected_population} mean")

        axis.set_ylabel("frequency")
        axis.set_xlabel("sample mean")

        st.pyplot(figure)
        plt.close(figure)

    population_mean = my.mean(*population)
    mean_of_sample_means = my.mean(*sample_means)

    with right:
        st.metric("population_mean", f"{population_mean:.4f}")
        st.metric("Mean of sample means", f"{mean_of_sample_means:.4f}")
