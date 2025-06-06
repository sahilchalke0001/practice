 121: Best Time to Buy and Sell Stock
class Solution(object):
    def maxProfit(self, prices):
       
        min_price = prices[0]  # Minimum price seen so far
        max_profit = 0            # Maximum profit seen so far

        for price in prices:
            if price < min_price:
                min_price = price  # Found a lower price to buy
            else:
                profit = price - min_price  # Calculate profit if sold today
                max_profit = max(max_profit, profit)  # Update max profit if better

        return max_profit

Time Complexity: O(n)
Space Complexity: O(1)