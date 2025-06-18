class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        res = []

        for elem in nums:
            num = elem
            temp = []

            while num != 0:
                temp.append(num % 10)
                num = num // 10
            
            res.extend(temp[-1::-1])
        
        return res