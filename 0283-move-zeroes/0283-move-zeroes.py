class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        idx = -1

        for i in range(len(nums)):
            if nums[i] != 0:
                idx += 1
                nums[idx], nums[i] = nums[i], nums[idx] 
        