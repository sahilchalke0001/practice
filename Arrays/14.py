LeetCode 134
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        
        total_tank = 0     # Total gas balance over entire route
        curr_tank = 0      # Current gas balance from starting point
        start_station = 0  # Potential starting index

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]

            # If we run out of gas before reaching station i+1
            if curr_tank < 0:
                # We cannot start from current start_station
                # So we try next station as new starting point
                start_station = i + 1
                curr_tank = 0  # Reset current tank for new start

        # If total gas is less than total cost, no solution
        if total_tank < 0:
            return -1
        else:
            return start_station
Time Complexity: O(n)
→ We traverse the list once.

Space Complexity: O(1)
→ No extra space is used except for a few variables.