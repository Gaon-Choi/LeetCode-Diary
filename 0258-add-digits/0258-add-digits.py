class Solution:
    def addDigits(self, num: int) -> int:
        ans = num
    
        while len(str(ans)) != 1:
            arr = list(map(int, list(str(ans))))
            ans = sum(arr)

        return ans