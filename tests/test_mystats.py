import pytest
import pandas as pd
import numpy as np
import src.mystats as my

def test_statistics_functions():

    values = np.random.default_rng().normal(size = 100)
    values2 = np.random.default_rng().normal(size = 100)
    indicator = np.random.default_rng().uniform(0, 100)

    assert my.mean(*values) == pytest.approx(
        np.mean(values)
    )

    assert my.median(*values) == pytest.approx(
        np.median(values)
    ) 

    '''
    assert my.mode(*values) == pytest.approx(
        np.mode(values)
    )
    '''

    assert my.data_range(*values) == pytest.approx(
        np.ptp(values)
    )

    assert my.std_variance(*values) == pytest.approx(
        np.var(values, ddof=0)
    )

    assert my.sample_variance(*values) == pytest.approx(
        np.var(values, ddof=1)
    )

    assert my.std_deviation(*values) == pytest.approx(
        np.std(values, ddof=0)
    )

    assert my.sample_deviation(*values) == pytest.approx(
        np.std(values, ddof=1)
    )

    assert my.percentile(indicator, *values) == pytest.approx(
        np.percentile(values, indicator, method="linear")
    )

    assert my.quartiles(1, *values) == pytest.approx(
        np.percentile(values, 25, method="linear")
    )

    assert my.quartiles(2, *values) == pytest.approx(
        np.percentile(values, 50, method="linear")
    )

    assert my.quartiles(3, *values) == pytest.approx(
        np.percentile(values, 75, method="linear")
    )

    '''
    assert my.quartiles(3, *values) == pytest.approx(
            np.percentile(values, 75, method="linear")
        )
    '''

    assert my.covariance(values, values2) == pytest.approx(
        np.cov(values, values2, ddof=0)[0, 1]
    )

    assert my.sample_covariance(values, values2) == pytest.approx(
        np.cov(values, values2, ddof=1)[0, 1]
    )

    assert my.pearson_correlation(values, values2) == pytest.approx(
            np.corrcoef(values, values2)[0, 1]
    )

    assert my.iqr(*values) == pytest.approx(
        np.percentile(values, 75, method="linear") - np.percentile(values, 25, method="linear")
    )

    '''
    assert my.get_outliers(*values) == pytest.approx(
        np.algum.algo
    )
    '''
