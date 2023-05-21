from Roman_to_Integer import Solution
import pytest


@pytest.mark.parametrize(
    "a, expected_result", [("III", 3), ("LVIII", 58), ("MCMXCIV", 1994)]
)
def test_intToRoman_good(a, expected_result):
    assert Solution.romanToInt("", a) == expected_result
