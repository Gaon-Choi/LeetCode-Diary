from collections import defaultdict

class Solution:
    def maxFreqSum(self, s: str) -> int:
        vowel = {
            "a": 0,
            "e": 0,
            "i": 0,
            "o": 0,
            "u": 0
        }

        dd = defaultdict(int)

        for c in s:
            if c in vowel:
                vowel[c] += 1
            else:
                dd[c] += 1
        
        return max(list(dd.values()) + [0]) + max(list(vowel.values()) + [0])

