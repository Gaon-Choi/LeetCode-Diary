class Solution:
    def isHappy(self, n: int) -> bool:
        arr = [n]
        num = n

        while True:
            arr_ = list(map(int, list(str(num))))

            num = sum(x**2 for x in arr_)

            if num == 1:
                return True

            if num in arr:
                break
            else:
                arr.append(num)

        return False