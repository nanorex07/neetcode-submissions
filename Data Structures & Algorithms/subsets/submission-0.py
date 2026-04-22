class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        sol = []
        def create(i: int, current: List[int]):
            if i == len(nums):
                sol.append([x for x in current])
                return
            
            current.append(nums[i])
            create(i+1, current)
            current.pop()
            create(i+1, current)
        create(0, [])
        return sol