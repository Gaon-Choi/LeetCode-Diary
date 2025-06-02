class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        for idx in range(1 << len(nums)):
            temp = []

            for i in range(len(nums)):
                if idx & (1 << i) > 0:
                    temp.append(nums[i])

            result.append(temp)

        return result
        