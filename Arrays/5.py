Leetcode 169. Majority Element
class Solution:
    def majorityElement(self, nums):
        
        count = 0
        candidate = None

        for num in nums:
            if count == 0:
                candidate = num  # Choose new candidate

            # Increase or decrease the count
            if num == candidate:
                count += 1
            else:
                count -= 1

        # Since it's guaranteed that a majority element exists, we return the candidate
        return candidate


Boyer-Moore Voting Algorithm
Time Complexity: O(n)
Space Complexity: O(1)
        