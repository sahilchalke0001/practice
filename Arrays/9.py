55. Jump Game
class Solution(object):
    def canJump(self, nums):
        max_reach = 0  # The farthest index we can reach

        for i in range(len(nums)):
            if i > max_reach:
                return False  # Current position is unreachable
            max_reach = max(max_reach, i + nums[i])  # Update max reach

        return True  # We can reach the end

Time Complexity: O(n)
Space Complexity: O(1)