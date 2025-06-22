import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        pq = []

        for elem in nums:
            heapq.heappush(pq, -elem)

        for _ in range(k - 1):
            heapq.heappop(pq)

        return -pq[0]