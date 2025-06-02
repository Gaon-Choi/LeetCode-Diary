class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        result = []
        combi = []

        arr = list(range(1, n + 1))

        def backtrack(start):
            if len(combi) == k:
                result.append(combi[:])
                return

            for i in range(start, n):
                combi.append(arr[i])
                backtrack(i + 1)
                combi.pop()

        backtrack(0)

        return result
        