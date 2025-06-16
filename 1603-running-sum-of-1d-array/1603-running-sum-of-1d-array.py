class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        res = []

        for elem in nums:
            if res:
                res.append(res[-1] + elem)
            else:
                res.append(elem)

        return res
        