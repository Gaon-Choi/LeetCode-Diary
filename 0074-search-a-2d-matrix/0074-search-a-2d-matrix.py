class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = 0
        col = 0

        for i in range(1, len(matrix)):
            if matrix[i][0] > target:
                break
            else:
                row = i

        for i in range(len(matrix[0])):
            if matrix[row][i] == target:
                return True
            elif matrix[row][i] > target:
                return False

        return False