class Solution:
    def smallestIndex(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            sum_ = sum(map(int, list(str(nums[i]))))

            if sum_ == i:
                return i
        
        return -1
        