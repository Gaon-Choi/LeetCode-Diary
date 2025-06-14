from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maxi = len(nums) // 2

        cnt = defaultdict(int)

        for elem in nums:
            cnt[elem] += 1

            if cnt[elem] > maxi:
                return elem