class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        
        dp = [0]*len(nums)
        dp[0]=1

        for j in range(1, len(nums)):
            dp[j] = 1
            for i in range(j):
                if nums[i] < nums[j]:
                    dp[j] = max(dp[i]+1, dp[j])
        return max(dp)