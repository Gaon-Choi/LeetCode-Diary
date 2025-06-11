class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        arr = list(map(int, list(str(n))))

        a, b = 1, 0

        for elem in arr:
            a *= elem
            b += elem

        return a - b
                