class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        res = 0

        for elem in nums:
            if elem % 3 != 0:
                res += 1

        return res
        