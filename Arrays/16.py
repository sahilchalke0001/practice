42. Trapping Rain Water 
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0  # Edge case: empty list, no water

        l, r = 0, len(height) - 1  # Two pointers
        leftMax, rightMax = height[l], height[r]  # Track max heights from both ends
        res = 0  # Accumulated trapped water

        while l < r:
            if leftMax < rightMax:
                # Move left pointer inward
                l += 1
                leftMax = max(leftMax, height[l])  # Update max on left
                res += leftMax - height[l]  # Water trapped = leftMax - current height
            else:
                # Move right pointer inward
                r -= 1
                rightMax = max(rightMax, height[r])  # Update max on right
                res += rightMax - height[r]  # Water trapped = rightMax - current height

        return res


Time Complexity: O(n)
→ One pass using two pointers.

Space Complexity: O(1)
→ Constant extra space.