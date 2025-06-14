class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        allowed_s = set(list(allowed))

        cnt = len(words)

        for word in words:
            for c in word:
                if c not in allowed_s:
                    cnt -= 1
                    break

        return cnt
