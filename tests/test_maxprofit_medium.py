from Maxprofit_medium import Solution
import pytest


@pytest.mark.parametrize(
    "a, expected_result",
    [([7, 1, 5, 3, 6, 4], 7), ([1, 2, 3, 4, 5], 4), ([7, 6, 4, 3, 1], 0)],
)
def test_maxprofit_medium_good(a, expected_result):
    assert Solution.maxProfit("", a) == expected_result
