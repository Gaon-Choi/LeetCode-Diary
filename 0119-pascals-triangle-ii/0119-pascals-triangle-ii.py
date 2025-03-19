class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        result = []

        for i in range(1, rowIndex + 2):
            if i == 1:
                result.append([1])
            else:
                result.append([1] + [0] * (i - 2) + [1])

        for i in range(2, rowIndex + 1):
            for j in range(1, i):
                result[i][j] = result[i-1][j-1] + result[i-1][j]

        return result[-1]