27. Remove Element
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer to track the next position to place non-val element
        k = 0  

        # Traverse the entire array
        for i in range(len(nums)):
            if nums[i] != val:
                # If current element is not val, place it at index k
                nums[k] = nums[i]
                k += 1  # Increment k for next placement

        # After loop, k is the new length of the array without `val`
        return k

Time Complexity: O(n)
Every element is visited once.

Space Complexity: O(1)
No extra space is used; the operation is done in-place.