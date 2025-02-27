class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        str_reversed_x = str_x[-1::-1]

        return str_x == str_reversed_x