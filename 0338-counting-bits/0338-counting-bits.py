class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []

        for i in range(n + 1):
            binary_num = str(bin(i))[2:].count('1')
            ans.append(binary_num)

        return ans

        