from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dd = defaultdict(int)

        for elem in nums:
            dd[elem] += 1

        arr = list(dd.items())

        arr.sort(key = lambda x : -x[1])

        return [x[0] for x in arr[:k]]