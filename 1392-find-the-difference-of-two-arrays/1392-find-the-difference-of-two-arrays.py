class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        hash1 = dict()
        hash2 = dict()
        
        for elem in nums1:
            if elem not in hash1:
                hash1[elem] = 1

        for elem in nums2:
            if elem not in hash2:
                hash2[elem] = 1

        arr1 = []
        arr2 = []

        for elem in nums1:
            if elem not in hash2:
                arr1.append(elem)

        for elem in nums2:
            if elem not in hash1:
                arr2.append(elem)

        return [list(set(arr1)), list(set(arr2))]