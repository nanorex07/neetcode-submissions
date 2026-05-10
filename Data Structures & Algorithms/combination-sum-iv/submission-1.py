class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        memo = {0: 1}
    
        for tr in range(1, target+1):
            memo[tr] = 0
            for num in nums:
                if tr >= num:
                    memo[tr]+=memo[tr-num]
        return memo[target]
                