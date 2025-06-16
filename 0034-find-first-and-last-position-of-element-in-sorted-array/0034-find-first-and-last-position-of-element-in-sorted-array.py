class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def lower_bound(arr, k):
            left, right = 0, len(arr) - 1

            min_idx = len(arr)

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] >= k:
                    right = mid - 1
                    min_idx = min(min_idx, mid)
                else:
                    left = mid + 1

            return min_idx

        def upper_bound(arr, k):
            left, right = 0, len(arr) - 1

            min_idx = len(arr)

            while left <= right:
                mid = (left + right) // 2

                if arr[mid] > k:
                    right = mid - 1
                    min_idx = min(min_idx, mid)
                else:
                    left = mid + 1

            return min_idx

        lb, ub = lower_bound(nums, target), upper_bound(nums, target)

        if lb == ub:
            return [-1, -1]
        else:
            return [lb, ub - 1]

        