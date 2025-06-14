class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        zeros = s.count("0")

        ones = len(s) - zeros - 1

        return ones * "1" + zeros * "0" + "1"
        