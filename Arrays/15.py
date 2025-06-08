135. Candy
class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        candies = [1] * n  # Step 1: Give 1 candy to everyone initially

        # Left to Right: Ensure increasing rating gets more candy
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1

        # Right to Left: Ensure higher rated kids get more than next if needed
        for i in range(n - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        # Return total candies distributed
        return sum(candies)

Time and Space Complexity:
Time Complexity: O(n)
→ Two passes over the array.

Space Complexity: O(n)
→ Extra space for the candies array.