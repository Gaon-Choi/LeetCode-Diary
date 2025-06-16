class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        ans = 0

        while numOnes > 0 and k > 0:
            numOnes -= 1
            k -= 1
            ans += 1

        while numZeros > 0 and k > 0:
            numZeros -= 1
            k -= 1
        
        while numNegOnes > 0 and k > 0:
            numNegOnes -= 1
            k -= 1
            ans -= 1

        return ans