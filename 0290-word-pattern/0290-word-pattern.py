class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        key = list(pattern)
        words = s.split()

        hash1 = dict()
        hash2 = dict()

        if len(key) != len(words):
            return False

        for i in range(len(key)):
            if key[i] in hash1:
                if hash1[key[i]] == words[i]:
                    continue
                else:
                    return False
            else:
                hash1[key[i]] = words[i]

            if words[i] in hash2:
                if hash2[words[i]] == key[i]:
                    continue
                else:
                    return False
            else:
                hash2[words[i]] = key[i]

        return True