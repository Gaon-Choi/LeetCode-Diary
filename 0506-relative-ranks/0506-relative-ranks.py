class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        pq = []

        for elem in score:
            heapq.heappush(pq, -elem)

        hash_ = dict()

        for i in range(len(score)):
            elem = -heapq.heappop(pq)
            hash_[elem] = i + 1

        result = []

        for elem in score:
            result_ = hash_[elem]

            if result_ == 1:
                result.append("Gold Medal")
            elif result_ == 2:
                result.append("Silver Medal")
            elif result_ == 3:
                result.append("Bronze Medal")
            else:
                result.append(str(result_))

        return result        