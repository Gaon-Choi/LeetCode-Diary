class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        s_arr = [0]

        for elem in arr:
            s_arr.append(s_arr[-1] + elem)

        num = 1

        size = len(arr)

        ans = 0

        while num <= size:
            for offset in range(size - num + 1):
                ans += (s_arr[offset + num] - s_arr[offset])

            num += 2

        return ans
