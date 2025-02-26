class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx1 = 0; idx2 = 0
        idx = 0

        temp_arr = nums1[:m]

        while idx1 < m and idx2 < n:
            if temp_arr[idx1] <= nums2[idx2]:
                nums1[idx] = temp_arr[idx1]
                idx1 += 1
            else:
                nums1[idx] = nums2[idx2]
                idx2 += 1
            
            idx += 1

        while idx1 < m:
            nums1[idx] = temp_arr[idx1]
            idx += 1
            idx1 += 1

        while idx2 < n:
            nums1[idx] = nums2[idx2]
            idx += 1
            idx2 += 1
