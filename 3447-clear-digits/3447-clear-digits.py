class Solution:
    def clearDigits(self, s: str) -> str:
        size = len(s)

        is_deleted = [False] * size

        for i in range(size):
            if s[i].isnumeric():
                is_deleted[i] = True

                j = i - 1

                while j >= 0:
                    if not is_deleted[j]:
                        is_deleted[j] = True
                        break

                    j -= 1

        res = ""

        for i in range(size):
            if not is_deleted[i]:
                res += s[i]

        return res