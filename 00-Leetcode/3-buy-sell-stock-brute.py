class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j]-prices[i]
                max_profit = max(max_profit, profit)
        
        return max_profit
    