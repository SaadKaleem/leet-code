"""
06/05/2022 - https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

Runtime: 983 ms, faster than 96.99% of Python3 online submissions for Best Time to Buy and Sell Stock.
Memory Usage: 25.1 MB, less than 37.02% of Python3 online submissions for Best Time to Buy and Sell Stock.
"""

from typing import List 

"""
For n elements in the list
Time complexity: O(n)
Space complexity: O(1)
"""

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        buy_price = prices[0]
        max_profit = 0
        
        for current_price in prices[1:]:
            if buy_price > current_price:
                buy_price = current_price
            elif (current_price - buy_price) > max_profit:
                max_profit = current_price - buy_price
                
        return max_profit
            