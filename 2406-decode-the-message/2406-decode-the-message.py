class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        ans = ""

        cipher = dict()

        num = ord('a')

        for c in key:
            if not c.isalpha():
                continue

            if c in cipher:
                continue

            cipher[c] = chr(num)

            num += 1

        for c in message:
            if c not in cipher:
                ans += c
            else:
                ans += cipher[c]

        return ans
        