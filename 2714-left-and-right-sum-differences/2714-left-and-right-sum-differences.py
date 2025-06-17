class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        left_sum = [0]
        right_sum = [0]

        for i in range(len(nums)):
            left_sum.append(left_sum[-1] + nums[i])

        for i in range(len(nums)):
            right_sum = [nums[-i - 1] + right_sum[0]] + right_sum

        left_sum = left_sum[1:]
        right_sum = right_sum[:-1]
    
        return list(map(lambda x : abs(x[0] - x[1]), zip(left_sum, right_sum)))
