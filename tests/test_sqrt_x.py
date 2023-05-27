from sqrt_x import Solution
import pytest


@pytest.mark.parametrize("a, expected_result", [(4, 2), (8, 2)])
def test_sqrt_good(a, expected_result):
    assert Solution.mySqrt("", a) == expected_result
