from Integer_to_Roman import Solution
import pytest


@pytest.mark.parametrize(
    "a, expected_result", [(3, "III"), (58, "LVIII"), (1994, "MCMXCIV")]
)
def test_intToRoman_good(a, expected_result):
    assert Solution.intToRoman("", a) == expected_result
