class Solution:
    def balancedStringSplit(self, s: str) -> int:
        balance = 0
        cnt = 0

        for c in s:
            if c == "R":
                balance += 1
            else:
                balance -= 1

            if balance == 0:
                cnt += 1

        return cnt
        