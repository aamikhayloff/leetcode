from isvalid import Solution
import pytest


@pytest.mark.parametrize(
    "a, expected_result", [("()", True), ("()[]{}", True), ("}[", False)]
)
def test_isvalid_good(a, expected_result):
    assert Solution.isValid("", a) == expected_result
