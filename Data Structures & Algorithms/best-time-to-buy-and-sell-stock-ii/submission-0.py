class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        dp = [0]*len(prices)
        
        for i in range(1, len(prices)):
            for j in range(0, i):
                dp[i] = max(dp[i], dp[j]+prices[i]-prices[j], dp[j])
        return dp[-1]