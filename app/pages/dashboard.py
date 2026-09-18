import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st

import src.mystats as my

continuos_data = ["temp", "atemp", "hum", "windspeed"]
non_numeric_data = ["dteday"]

data = pd.read_csv("./data/hour.csv")

left, center, right = st.columns(
    [1, 2.5, 1],
    gap="large",
)


with center:
    selected_variable = st.selectbox(
        "Select a variable",
        options=data.columns.tolist(),
    )

    selected_data = data[selected_variable]

    if selected_variable in continuos_data:
        selected_data = pd.cut(selected_data, bins=5)

        frequency_table = (
            selected_data.value_counts()
            .sort_index()
            .rename_axis("class")
            .reset_index(name="frequency")
        )

        frequency_table["class"] = frequency_table["class"].map(
            lambda interval: f"{interval.left:.2f}–{interval.right:.2f}"
        )

    else:
        frequency_table = (
            selected_data.value_counts()
            .sort_index()
            .rename_axis("class")
            .reset_index(name="frequency")
        )

    st.dataframe(
        frequency_table,
        column_config={
            "class": st.column_config.TextColumn(
                "Class",
                alignment="left",
            ),
            "frequency": st.column_config.NumberColumn(
                "Frequency",
                alignment="left",
            ),
        },
        hide_index=True,
    )

if selected_variable not in non_numeric_data:
    values = data[selected_variable].dropna().tolist()

    with center:
        summary_table = pd.DataFrame(
            [
                [
                    my.mean(*values),
                    my.median(*values),
                    my.mode(*values),
                    my.std_variance(*values),
                    my.std_deviation(*values),
                    my.data_range(*values),
                    my.quartiles(1, *values),
                    my.quartiles(3, *values),
                    my.iqr(*values),
                ]
            ],
            columns=[
                "mean",
                "median",
                "mode",
                "variance",
                "std_deviation",
                "range",
                "q1",
                "q3",
                "iqr",
            ],
        )

        st.subheader("Summary Statistics")
        st.dataframe(
            summary_table,
            column_config={
                "mean": st.column_config.TextColumn(
                    "Mean",
                    alignment="center",
                ),
                "median": st.column_config.NumberColumn(
                    "Median",
                    alignment="center",
                ),
                "mode": st.column_config.NumberColumn(
                    "Mode",
                    alignment="center",
                ),
                "variance": st.column_config.TextColumn(
                    "Variance",
                    alignment="center",
                ),
                "std_deviation": st.column_config.NumberColumn(
                    "Std Deviation",
                    alignment="center",
                ),
                "range": st.column_config.NumberColumn(
                    "Range",
                    alignment="center",
                ),
                "q1": st.column_config.NumberColumn(
                    "Q1",
                    alignment="center",
                ),
                "q3": st.column_config.NumberColumn(
                    "Q3",
                    alignment="center",
                ),
                "iqr": st.column_config.NumberColumn(
                    "IQR",
                    alignment="center",
                ),
            },
            hide_index=True,
        )

        outliers_table = pd.DataFrame(
            [
                [
                    my.get_outliers(*values)["lower_fence"],
                    my.get_outliers(*values)["upper_fence"],
                    len(my.get_outliers(*values)["lower_outliers"]),
                    len(my.get_outliers(*values)["upper_outliers"]),
                ]
            ],
            columns=[
                "lower_fence",
                "upper_fence",
                "lower_outliers",
                "upper_outliers",
            ],
        )

        st.subheader("Outliers Detection")
        st.dataframe(
            outliers_table,
            column_config={
                "lower_fence": st.column_config.TextColumn(
                    "Lower Fence",
                    alignment="center",
                ),
                "upper_fence": st.column_config.NumberColumn(
                    "Upper Fence",
                    alignment="center",
                ),
                "lower_outliers": st.column_config.NumberColumn(
                    "Lower Outliers",
                    alignment="center",
                ),
                "upper_outliers": st.column_config.TextColumn(
                    "Upper Outliers",
                    alignment="center",
                ),
            },
            hide_index=True,
        )

    with left:
        st.title("Automatic Text Interpretation")
        tolerance_user_value = st.slider(
            "Tolerance = selected_value * std_deviation",
            min_value=0.0,
            max_value=1.0,
            value=0.2,
            step=0.05,
        )
        tolerance = tolerance_user_value * my.std_deviation(*values)

        if abs(my.mean(*values) - my.median(*values)) <= tolerance:
            st.subheader("Aproximadamente simétrico")
        elif my.mean(*values) - my.median(*values) > tolerance:
            st.subheader("Positivo | Assimétrico à direita")
        elif (my.mean(*values) - my.median(*values)) < -tolerance:
            st.subheader("Negativo | Assimétrico à esquerda")

    with right:
        st.title("Graphs")

        figure_hist, axis_hist = plt.subplots(figsize=(10, 4))
        axis_hist.set_title("Distribution")
        axis_hist.set_xlabel(selected_variable)
        axis_hist.set_ylabel("frequency")
        axis_hist.hist(values, bins=5, edgecolor="black")
        st.pyplot(figure_hist)
        plt.close(figure_hist)

        figure_box, axis_box = plt.subplots(figsize=(10, 4))
        axis_box.set_title("Boxplot")
        axis_box.set_xlabel(selected_variable)
        axis_box.boxplot(values, vert=False)
        st.pyplot(figure_box)
        plt.close(figure_box)

else:
    with center:
        st.info(
            "Central-tendency, dispersion, outlier detection, "
            "and numeric graphs are unavailable for this variable."
        )
