class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        cnt = 0

        for elem in hours:
            if elem >= target:
                cnt += 1

        return cnt
        