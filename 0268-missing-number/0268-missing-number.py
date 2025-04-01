class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        num_list = range(len(nums) + 1)

        hash_dict = dict(zip(num_list, [0] * len(num_list)))

        for elem in nums:
            del hash_dict[elem]

        val = list(hash_dict.keys())

        return val[0]
        