from Longest_common_prefix import Solution
import pytest


@pytest.mark.parametrize(
    "a, expected_result",
    [(["flower", "flow", "flight"], "fl"), (["dog", "racecar", "car"], "")],
)
def test_longest_common_prefix_good(a, expected_result):
    assert Solution.longestCommonPrefix("", a) == expected_result
