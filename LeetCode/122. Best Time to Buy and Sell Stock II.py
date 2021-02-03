# 2021-02-04
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total_profit = 0
        previous = 10**4
        
        for price in prices:
            if price - previous > 0:
                profit = price - previous
                total_profit += profit 
                
            previous = price
            
        return total_profit
            
        
