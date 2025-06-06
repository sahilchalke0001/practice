80. Remove Duplicates from Sorted Array II
from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # If the list has 2 or fewer elements, it's already valid
        if len(nums) <= 2:
            return len(nums)

        # 'i' is the pointer where we place allowed values
        i = 2

        # Start from index 2 since first two can always stay
        for j in range(2, len(nums)):
            # Check if the current number is not the same as nums[i-2]
            # This ensures each element appears at most twice
            if nums[j] != nums[i - 2]:
                nums[i] = nums[j]
                i += 1

        return i  # 'i' is the new length of the array

Time and Space Complexity:
Time Complexity: O(n)
One pass through the array.

Space Complexity: O(1)
Done in-place without extra memory.