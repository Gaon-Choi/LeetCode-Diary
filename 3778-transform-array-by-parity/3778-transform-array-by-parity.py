class Solution:
    def transformArray(self, nums: List[int]) -> List[int]:
        even, odd = 0, 0

        for elem in nums:
            if elem & 1 == 1:
                odd += 1
            else:
                even += 1

        return [0] * even + [1] * odd
        