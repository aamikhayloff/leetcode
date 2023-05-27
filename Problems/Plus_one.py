from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        str_1 = "".join(map(str, digits))
        str_1 = int(str_1)
        str_2 = str_1 + 1
        return map(int, str(str_2))
