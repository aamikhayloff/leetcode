import pytest

from Palindrome_number import Solution

@pytest.mark.parametrize("x, expected_result", [(1221, True),
                                                (12211, False),
                                                ('False', False),
                                                ('ABCDCBA', True)])
def test_palindome_number_good(x, expected_result):
    assert Solution.isPalindrome("", x) == expected_result