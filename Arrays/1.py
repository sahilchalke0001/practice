88. Merge Sorted Array
from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # Start filling nums1 from the end
        i = m - 1  # Pointer for end of actual elements in nums1
        j = n - 1  # Pointer for end of nums2
        k = m + n - 1  # Pointer for the end of nums1's total length

        # Merge while both arrays have elements to compare
        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If nums2 still has elements left, copy them to nums1
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1


Time and Space Complexity:
Time Complexity: O(m + n)
You compare and place each element once.

Space Complexity: O(1)
You do it in-place using constant extra space.