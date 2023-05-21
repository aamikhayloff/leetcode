from strs import Solution
import pytest


@pytest.mark.parametrize(
    "a, b, expected_result", [("sadbutsad", "sad", 0), ("leetcode", "leeto", -1)]
)
def test_strs_good(a, b, expected_result):
    assert Solution.strStr("", a, b) == expected_result
