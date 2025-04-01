from collections import deque

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        cnt = 0

        dxs = [1, 0, -1, 0]
        dys = [0, 1, 0, -1]

        m, n = len(grid), len(grid[0])
        visited = [[False] * n for _ in range(m)]

        def is_reachable(x, y):
            return 0 <= x < m and 0 <= y < n and grid[x][y] == "1"

        def bfs(x_, y_):
            queue = deque([[x_, y_]])
            visited[x_][y_] = True

            while queue:
                x, y = queue.popleft()

                for dx, dy in zip(dxs, dys):
                    nx, ny = x + dx, y + dy
                    if is_reachable(nx, ny) and not visited[nx][ny]:
                        visited[nx][ny] = True
                        queue.append([nx, ny])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1" and not visited[i][j]:
                    bfs(i, j)
                    cnt += 1

        return cnt