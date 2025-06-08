238. Product of Array Except Self
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        n = len(nums)
        answer = [1] * n  # Initialize output array with 1s

        # Step 1: Left pass
        # answer[i] will contain product of all elements to the left of i
        left_product = 1
        for i in range(n):
            answer[i] = left_product
            left_product *= nums[i]  # Update left product for next index

        # Step 2: Right pass
        # Multiply answer[i] by product of all elements to the right of i
        right_product = 1
        for i in range(n - 1, -1, -1):
            answer[i] *= right_product
            right_product *= nums[i]  # Update right product for next index

        return answer
t-O(n)
s-(1)