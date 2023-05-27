class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split()
        last = words[-1]
        last_list = list(last)
        return len(last_list)
