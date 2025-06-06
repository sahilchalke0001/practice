45. Jump Game II
class Solution(object):
    def jump(self, nums):
        jumps = 0           # Number of jumps needed
        farthest = 0        # The farthest we can go in current window
        current_end = 0     # End of the current jump range

        for i in range(len(nums) - 1):  # We don't need to jump from the last index
            farthest = max(farthest, i + nums[i])  # Update max reachable
            if i == current_end:  # Time to make a jump
                jumps += 1
                current_end = farthest  # Set new range

        return jumps
Time Complexity: O(n)
Space Complexity: O(1)