class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_ = ''.join(sorted(list(s)))
        t_ = ''.join(sorted(list(t)))

        return s_ == t_