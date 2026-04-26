class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        res = []

        nums.sort()

        for i in range(len(nums)):
            if i > 0 and nums[i]==nums[i-1]:
                continue
            j = i+1
            k = len(nums)-1
            target = -nums[i]
            while k > j:
                if nums[j]+nums[k] < target:
                    j+=1
                elif nums[j]+nums[k] > target:
                    k-=1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j+=1
                    k-=1
                    while nums[j]==nums[j-1] and j < k:
                        j+=1
        return res