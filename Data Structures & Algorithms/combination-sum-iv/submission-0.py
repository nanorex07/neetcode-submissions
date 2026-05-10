class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        nums.sort()
        memo = {0: 1}

        def solve(target: int):
            if target in memo:
                return memo[target]
            res = 0
            for num in nums:
                if target < num:
                    break
                res += solve(target-num)
            memo[target] = res
            return res
        
        return solve(target)