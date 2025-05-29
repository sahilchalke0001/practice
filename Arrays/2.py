# 217. Contains Duplicate

# Input: nums = [1, 2, 3, 3]

# Output: true

class Solution(object):
    def containsDuplicate(self, nums):
        
        nums.sort()
        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                return True
        return False

Time & Space Complexity
Time complexity: 
O(nlogn)
Space complexity: 
O(1) or O(n) depending on the sorting algorithm.

class Solution(object):
    def containsDuplicate(self, nums):
        s=set(nums)
        if len(s)==len(nums):
            return False
        else:
            return True

T-O(n)
S-O(n)