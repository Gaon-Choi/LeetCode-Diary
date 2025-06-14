class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        res = []
        s = set()

        for elem in nums:
            if elem not in s:
                s.add(elem)
            else:
                res.append(elem)

        return res