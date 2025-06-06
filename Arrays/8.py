Leetcode 122 – Best Time to Buy and Sell Stock II
class Solution(object):
    def maxProfit(self, prices):
        
        profit = 0

        # Loop through the array from day 1 to the end
        for i in range(1, len(prices)):
            # If today's price is greater than yesterday's, we can make a profit
            if prices[i] > prices[i - 1]:
                profit += prices[i] - prices[i - 1]

        return profit
Greedy approach: Add profit every time there's an increase.
Time Complexity: O(n)
Space Complexity: O(1)