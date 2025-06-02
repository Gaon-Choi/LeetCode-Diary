class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        ans = [-1, -1]
        for i in range(size):
            ans[0] = i
            for j in range(i+1, size):
                if nums[i]+nums[j]==target:
                    ans[1] = j
                    return ans