from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Initialize the variable to track the best day to buy (lowest price day) as the first day
        buy_day = 0
        # Initialize the maximum profit as 0
        max_profit = 0

        # Loop through each day starting from the second day
        for i in range(1, len(prices)):
            # If the current price is lower than the price on the recorded buy day, update buy_day
            if prices[i] < prices[buy_day]:
                buy_day = i
            # Otherwise, calculate the profit if sold on the current day and update max_profit if it's higher
            elif prices[i] - prices[buy_day] > max_profit:
                max_profit = prices[i] - prices[buy_day]

        # Return the maximum profit found
        return max_profit

# Time Complexity: O(n), where n is the number of days (length of the prices list).
# This is because we only iterate through the list once.

# Space Complexity: O(1), as we are using a constant amount of extra space regardless of the input size.
