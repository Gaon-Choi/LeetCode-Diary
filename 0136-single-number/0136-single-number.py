class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash = dict()

        for elem in nums:
            if elem in hash:
                del hash[elem]
            else:
                hash[elem] = 1

        return list(hash.keys())[0]