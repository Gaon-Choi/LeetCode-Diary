from collections import defaultdict

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hh = defaultdict(int)

        for c in magazine:
            hh[c] += 1

        for c in ransomNote:
            hh[c] -= 1

        for k, v in hh.items():
            if v < 0:
                return False

        return True
