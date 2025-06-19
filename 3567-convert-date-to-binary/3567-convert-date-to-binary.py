class Solution:
    def convertDateToBinary(self, date: str) -> str:
        days = list(map(int, date.split("-")))

        for i in range(len(days)):
            temp = days[i]
            res = ""

            while temp > 0:
                res += str(temp % 2)
                temp = temp // 2

            days[i] = res[-1::-1]

        return "-".join(days)