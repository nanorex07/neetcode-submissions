class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        res = []
        for a in range(len(nums)):
            if a>0 and nums[a-1] == nums[a]:
                continue
            for b in range(a+1, len(nums)):
                if b>a+1 and nums[b-1]==nums[b]:
                    continue
                
                c = b+1
                d = len(nums)-1
                find = target - nums[a] - nums[b]
                while d > c:
                    if nums[c] + nums[d] < find:
                        c+=1
                    elif nums[c] + nums[d] > find:
                        d-=1
                    else:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c+=1
                        d-=1
                        while nums[c-1] == nums[c] and c < d:
                            c+=1
        return res

# -3 0 1 2 3 3

