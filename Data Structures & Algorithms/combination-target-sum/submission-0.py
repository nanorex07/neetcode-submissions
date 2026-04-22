class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        sol = []
        
        def solve(i: int, current: List[int]):
            if sum(current) == target:
                sol.append([x for x in current])
                return
            if i == len(nums) or sum(current) > target:
                return
            
            solve(i+1, current)

            current.append(nums[i])
            solve(i, current)
            current.pop()
        
        solve(0, [])

        return sol