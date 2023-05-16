class Solution:
    def isValid(self, s: str) -> bool:
        res = []
        for i in s:
            if not res:
                res.append(i)

            elif (
                (i == ")" and res[-1] == "(")
                or (i == "]" and res[-1] == "[")
                or (i == "}" and res[-1] == "{")
            ):
                res.pop()
            else:
                res.append(i
        if not res:
            return True
        else:
            return False
