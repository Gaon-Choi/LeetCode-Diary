class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        max_size = max(len(matrix), len(matrix[0]))

        points = []

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    points.append((i, j))

        for p in points:
            x, y = p

            for dx, dy in ([(1, 0), (-1, 0), (0, 1), (0, -1)]):
                for mul in range(max_size):
                    nx, ny = x + mul * dx, y + mul * dy

                    if 0 <= nx < len(matrix) and 0 <= ny < len(matrix[0]):
                        matrix[nx][ny] = 0
                    else:
                        break

        return matrix