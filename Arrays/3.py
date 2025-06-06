26. Remove Duplicates from Sorted Array
class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        # Initialize the slow pointer at index 0
        i = 0  

        # Fast pointer starts from index 1
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                # Found a new unique element
                i += 1         # Move slow pointer
                nums[i] = nums[j]  # Replace with unique element

        return i + 1 

Time and Space Complexity:
Time Complexity: O(n)
Each element is visited once.

Space Complexity: O(1)
It modifies the list in-place with no extra memory.

class Solution(object):
    def removeDuplicates(self, nums):
        # Use a set to remove duplicates, then sort it (since the original list is sorted)
        unique_nums = sorted(set(nums))  # ✅ Now it's indexable set does not have indexes...
        k = len(unique_nums)

        # Overwrite nums with unique values
        for i in range(k):
            nums[i] = unique_nums[i]

        return k

Time and Space Complexity:
Time Complexity: O(n)

Space Complexity: O(n)
