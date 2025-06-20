class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candy = max(candies)

        res = []

        for elem in candies:
            if elem + extraCandies >= max_candy:
                res.append(True)
            else:
                res.append(False)

        return res