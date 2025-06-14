class Solution:
    def reverseDegree(self, s: str) -> int:
        res = 0

        for idx, c in enumerate(s):
            res += (26 - ord(c) + ord("a")) * (idx + 1)

        return res
