class Solution:
    def isPalindrome(self, x):

        s = str(x)
        rev_s = s[::-1]

        if s == rev_s:
            return True

        else:
            return False
