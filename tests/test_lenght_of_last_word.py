from Lenght_of_last_word import Solution
import pytest


@pytest.mark.parametrize(
    "a, expected_result",
    [(("Hello World", 5), ("fly me to the moon", 4), ("luffy is still joyboy", 6))],
)
def test_lenght_good(a, expected_result):
    assert Solution.lengthOfLastWord("", a) == expected_result
