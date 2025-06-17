class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        or_sum = nums[0]
        size = len(nums)

        for i in range(1, size):
            or_sum = or_sum | nums[i]

        return or_sum * (2 ** (size - 1))