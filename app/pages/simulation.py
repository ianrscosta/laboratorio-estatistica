import matplotlib.pyplot as plt
import numpy as np
import streamlit as st

left, center, right = st.columns([1, 2.5, 1])

with center:
    st.header("Law of Large Numbers")

    center_left, center_right = st.columns([1, 2])

    with center_left:
        selected_simulation = st.selectbox(
            "Select a simulation",
            options=["coin", "dice"],
        )

    with center_right:
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

        figure, axis = plt.subplots()
        axis.set_title("Results")
        axis.bar(
            ["Heads", "Tails"],
            [heads, tails],
        )
        axis.set_ylabel("frequency")
        st.pyplot(figure)
        plt.close(figure)

        figure, axis = plt.subplots()
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
