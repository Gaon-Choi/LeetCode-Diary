class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        def is_reachable(x, y):
            return 0 <= x < n and 0 <= y < n and (matrix[x][y] == 0)

        matrix = [[0] * n for _ in range(n)]

        dxs = [0, 1, 0, -1]
        dys = [1, 0, -1, 0]

        curr = 0
        x, y = 0, 0

        for num in range(1, n ** 2 + 1):
            matrix[x][y] = num

            if not is_reachable(x + dxs[curr], y + dys[curr]):
                curr = (curr + 1) % 4

            x += dxs[curr]
            y += dys[curr]

        return matrix
        