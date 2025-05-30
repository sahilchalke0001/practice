# 27. Remove Element 
# Input: nums = [1,1,2,3,4], val = 1

# Output: [2,3,4]

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

t-O(N)
s-O(1)