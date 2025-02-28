class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        for _ in range(k):
            elem = nums.pop(-1)
            nums.insert(0, elem)

        return nums