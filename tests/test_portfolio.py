import pytest
import numpy as np

from portfolio.portfolio import Portfolio


@pytest.fixture
def list_1000_portfolio():

    return [Portfolio(mu=0, std=0.1) for i in range(1000)]


def test_calc_annual_return(list_1000_portfolio):

    annual_returns = [p.calc_annual_return() for p in list_1000_portfolio]
    mean_annual_return = np.mean(annual_returns)

    assert mean_annual_return < 2
    assert mean_annual_return > 0
