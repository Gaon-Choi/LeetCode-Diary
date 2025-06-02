from collections import deque

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def bfs(x, y):
            visited[x][y] = True
            q = deque([(x, y)])

            cnt = 0

            while q:
                x, y = q.popleft()

                cnt += 1

                for dx, dy in zip([1, 0, -1, 0], [0, 1, 0, -1]):
                    nx, ny = x + dx, y + dy

                    if 0 <= nx < height and 0 <= ny < width and grid[nx][ny] == 1 and not visited[nx][ny]:
                        visited[nx][ny] = True
                        q.append((nx, ny))

            return cnt

        height, width = len(grid), len(grid[0])

        visited = [[False] * width for _ in range(height)]

        ans = 0

        for x in range(height):
            for y in range(width):
                if grid[x][y] == 1 and not visited[x][y]:
                    ans = max(ans, bfs(x, y))

        return ans

        