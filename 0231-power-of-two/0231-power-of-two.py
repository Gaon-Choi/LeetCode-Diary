class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        # bitwise operation
        return (n > 0) and (n & (n - 1) == 0)