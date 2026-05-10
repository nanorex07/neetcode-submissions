class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        cSum = 0
        maxSum = nums[0]
        for num in nums:
            if cSum < 0:
                cSum = 0
            cSum += num
            maxSum = max(maxSum, cSum)
        return maxSum
