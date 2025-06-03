class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        def get_dist(p1, p2):
            return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

        def find(x):
            if x == uf[x]:
                return x

            root_node = find(uf[x])
            uf[x] = root_node

            return root_node

        def union(x, y):
            X, Y = find(x), find(y)
            uf[Y] = X

        size = len(points)

        dist = []

        for i, p1 in enumerate(points):
            for j, p2 in enumerate(points):
                if i >= j:
                    continue

                dist.append((i + 1, j + 1, get_dist(p1, p2)))

        dist.sort(key = lambda x : x[2])

        uf = list(range(size + 1))

        mst = 0

        for edge in dist:
            x, y, cost = edge

            if find(x) != find(y):
                mst += cost
                union(x, y)

        return mst
