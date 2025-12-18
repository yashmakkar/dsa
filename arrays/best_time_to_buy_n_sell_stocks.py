"""
Problem: https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
Pattern: Sliding Window / Greedy
Time: O(n)
Space: O(1)
"""

from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        - We want to buy at the minimum price before selling.
        - Traverse the array and track the minimum price so far.
        - For each day, try selling on that day and update max profit.
        """
        min_price = float("inf")
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price-min_price)
            print(max_profit)

        return max_profit
            


if __name__ == "__main__":
    sol = Solution()

    test_cases = [
        ([7,1,5,3,6,4], 5),
        ([7,6,4,3,1], 0),
        ([2,3,1,4,6,7], 6),
        ([2,4,1], 2)
    ]

    for prices, expected in test_cases:
        result = sol.maxProfit(prices)
        print(result == expected)