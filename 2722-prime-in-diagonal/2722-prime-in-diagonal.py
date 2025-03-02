class Solution:
    def diagonalPrime(self, nums: List[List[int]]) -> int:
        def isPrime(nums: int):
            if nums < 2:
                return False

            for i in range(2, int(math.sqrt(nums)) + 1):
                if nums % i == 0:
                    return False

            return True

        arr = []

        for i in range(len(nums)):
            arr.append(nums[i][i])
            arr.append(nums[i][-(i+1)])

        arr.sort(reverse=True)

        for elem in arr:
            if isPrime(elem):
                return elem

        return 0