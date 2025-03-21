class Solution:
    def isValid(self, s: str) -> bool:
        size = 0

        stack = []

        for c in s:
            if c in ["(", "[", "{"]:
                stack.append(c)
            else:
                if c == ")":
                    if stack and stack[-1] == "(":
                        stack.pop()
                    else:
                        return False

                if c == "]":
                    if stack and stack[-1] == "[":
                        stack.pop()
                    else:
                        return False

                if c == "}":
                    if stack and stack[-1] == "{":
                        stack.pop()
                    else:
                        return False

        if len(stack) > 0:
            return False

        return True