class Solution:
    def addBinary(self, a: str, b: str) -> str:
        total = 0

        for weight, val in enumerate(a[-1::-1]):
            total += (2 ** weight) * int(val)

        for weight, val in enumerate(b[-1::-1]):
            total += (2 ** weight) * int(val)

        result = ""

        while total != 0:
            result += str(total % 2)
            total = total // 2

        if result == "":
            result = "0"

        return result[-1::-1]
        