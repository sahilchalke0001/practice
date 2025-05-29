# 1. Two Sum
# Input: 
# nums = [3,4,5,6], target = 7

# Output: [0,1]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = {}  # val -> index

        for i, n in enumerate(nums):
            indices[n] = i

        for i, n in enumerate(nums):
            diff = target - n
            if diff in indices and indices[diff] != i:
                return [i, indices[diff]]

T-O(n)
S-O(n)