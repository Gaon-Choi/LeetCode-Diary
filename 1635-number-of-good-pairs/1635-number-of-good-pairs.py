from collections import defaultdict

class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        def comb(num):
            if num < 2:
                return 0
            
            return num * (num - 1) // 2

        mm = defaultdict(int)

        for elem in nums:
            mm[elem] += 1

        arr = list(mm.values())

        res = 0

        for elem in arr:
            res += comb(elem)

        return res