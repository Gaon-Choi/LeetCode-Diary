class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcd(a, b):
            ans = 1
            for i in range(1, min(a, b) + 1):
                if a % i == 0 and b % i == 0:
                    ans = i

            return ans

        def lcd(a, b):
            return (a * b) // gcd(a, b)

        return lcd(n, 2)
