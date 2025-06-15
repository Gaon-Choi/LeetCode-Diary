class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        cnt = 0
        
        for elem in nums:
            if len(str(elem)) % 2 == 0:
                cnt += 1
                
        return cnt
        