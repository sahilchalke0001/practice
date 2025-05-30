# 169. Majority Element
# Input: nums = [5,5,1,1,1,5,5]

# Output: 5
Sorting
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]

Boyer-Moore Voting Algorithm
class Solution:
    def majorityElement(self, nums):
        res = count = 0

        for num in nums:
            if count == 0:
                res = num
            count += (1 if num == res else -1)
        return res