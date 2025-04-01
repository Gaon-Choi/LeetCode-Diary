class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        result = ""

        max_size = min(list(map(lambda x: len(x), strs)))

        for i in range(max_size):
            prev = strs[0][i]
            flag = True

            for j in range(len(strs)):
                if strs[j][i] != prev:
                    flag = False
                    break

            if not flag:
                break
            
            result += prev

        return result
        