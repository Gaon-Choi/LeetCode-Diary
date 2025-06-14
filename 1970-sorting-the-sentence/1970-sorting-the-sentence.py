class Solution:
    def sortSentence(self, s: str) -> str:
        arr = []

        s_arr = s.split()

        for elem in s_arr:
            for i in range(len(elem)):
                if elem[i].isnumeric():
                    arr.append((elem[:i], int(elem[i:])))

        arr.sort(key = lambda x : x[1])

        return " ".join(map(lambda x : x[0], arr))