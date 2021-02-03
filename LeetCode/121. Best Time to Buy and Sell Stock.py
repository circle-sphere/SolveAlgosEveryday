# 2021-02-04
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        min_prc = float('inf')
        
        for i in range(len(prices)):
            min_prc = min(min_prc, prices[i])
            profit = max(profit, prices[i]-min_prc)
            
        return profit
        
