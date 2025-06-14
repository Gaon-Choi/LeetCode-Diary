from collections import defaultdict

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        graph = defaultdict(int)

        max_cnt = len(edges)

        for a, b in edges:
            graph[a] += 1
            graph[b] += 1

            if graph[a] == max_cnt:
                return a

            if graph[b] == max_cnt:
                return b