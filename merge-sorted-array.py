from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i = j = 0
        while i < m + n and j < n:
            if nums1[i] <= nums2[j]:
                for k in range(i, i + m):
                    nums1[k + 1] = nums1[k]
                nums1[i] = nums2[j]
                j += 1
                i += 1
            i += 1
        print(nums1)
