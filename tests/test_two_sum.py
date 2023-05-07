from two_sum import Solution
import pytest



@pytest.mark.parametrize("a, b, expected_result", [([3,2,4], 6, [1, 2]),
                                                   ([3,3], 6, [0, 1]),
                                                   ([3,2], 6, [])])
def test_two_sum_good(a, b, expected_result):
   assert Solution.twoSum("", a, b) == expected_result

@pytest.mark.parametrize("expected_expection, enter, tar", [(TypeError, "2", "3"),
                                                            (TypeError, True, 9)])
def test_two_sum_with_error(expected_expection, enter, tar):
   with pytest.raises(expected_expection):
      Solution.twoSum(tar, enter)
