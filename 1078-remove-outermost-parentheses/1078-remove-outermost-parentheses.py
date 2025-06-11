class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        arr = []
        stk = []
        temp = ""

        for c in s:
            temp += c

            if c == "(":
                stk.append(c)
            else:
                if stk and stk[-1] == "(":
                    stk.pop()

            if len(stk) == 0:
                arr.append(temp)
                temp = ""

        ans = ""

        for res in arr:
            ans += res[1:-1]

        return ans