class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ans = 0
        buy, sell = 0, 1
        if len(prices) == 1:
            return ans
        
        while sell < len(prices):
            val = prices[sell]-prices[buy]
            ans = max(ans, val)
            if val < 0:
                buy=sell
            sell+=1
        return ans
            