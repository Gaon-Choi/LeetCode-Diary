class Solution:
    def countAsterisks(self, s: str) -> int:
        arr = [val for idx, val in enumerate(s.split('|')) if idx % 2 == 0]

        ans = 0

        for elem in arr:
            ans += elem.count('*')

        return ans