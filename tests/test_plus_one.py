from Plus_one import Solution
import pytest


@pytest.mark.parametrize(
    "a, expected_result",
    [([1, 2, 3], [1, 2, 4]), ([4, 3, 2, 1], [4, 3, 2, 2]), ([9], [1, 2])],
)
def test_plusone_good(a, expected_result):
    assert Solution.plusOne("", a) == expected_result
