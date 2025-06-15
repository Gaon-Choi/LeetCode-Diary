class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_cnt = 0
        
        temp = 0
        
        for elem in nums:
            if elem == 1:
                temp += 1
            else:
                max_cnt = max(max_cnt, temp)
                temp = 0
                
        max_cnt = max(max_cnt, temp)
        
        return max_cnt
        