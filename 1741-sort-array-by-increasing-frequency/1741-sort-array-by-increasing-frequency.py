from collections import defaultdict

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        mm = defaultdict(int)

        for elem in nums:
            mm[elem] += 1

        res = []

        kv = list(mm.items())
        kv.sort(key = lambda x: (x[1], -x[0]))
        
        for k, v in kv:
            res.extend([k] * v)

        return res