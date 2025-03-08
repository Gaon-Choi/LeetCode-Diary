class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = ""

        for c in s:
            if c.isalnum():
                if c.isalpha():
                    word += c.lower()
                else:
                    word += c

        return word == word[-1::-1]