class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        size, cnt = len(nums), 0

        for i in range(size):
            for j in range(i + 1, size):
                for k in range(j + 1, size):
                    if nums[j] - nums[i] == diff and nums[k] - nums[j] == diff:
                        cnt += 1

        return cnt