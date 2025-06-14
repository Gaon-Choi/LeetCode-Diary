class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        alphabet = dict()

        for c in range(26):
            alphabet[c] = chr(ord("A") + c)
        
        num = columnNumber

        res = ""

        while num > 0:
            res += alphabet[(num - 1) % 26]
            num = (num - 1) // 26

        if res == "":
            res += "A"

        return res[-1::-1]