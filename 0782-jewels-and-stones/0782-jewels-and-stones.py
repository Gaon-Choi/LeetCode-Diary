class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        mp = defaultdict(int)

        for c in stones:
            mp[c] += 1

        ans = 0

        for c in jewels:
            ans += mp[c]

        return ans
        