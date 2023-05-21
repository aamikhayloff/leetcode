from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        size = len(strs)
        s = sorted(strs)
        if s == 0:
            return ""
        if s == 1:
            return s[0]
        end = min(len(s[0]), len(s[-1]))
        i = 0
        while i < end and (s[0][i] == s[size - 1][i]):
            i += 1
        res = s[0][0:i]
        return res
