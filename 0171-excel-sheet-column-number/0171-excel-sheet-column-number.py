class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        res = 0

        alphabet = dict()

        for alpha in range(26):
            alphabet[chr(ord('A') + alpha)] = alpha + 1

        columnTitle = list(columnTitle[-1::-1])

        for weight, val in enumerate(columnTitle):
            res += (26 ** weight) * alphabet[val]
        
        return res