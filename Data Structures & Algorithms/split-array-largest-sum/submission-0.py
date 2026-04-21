class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        

        def predicate(sumLimit: int):
            splits = 1
            currs = 0
            for num in nums:
                currs+=num
                if currs>sumLimit:
                    splits+=1
                    currs=num
            return splits <= k

        l,r,ans = max(nums), sum(nums), 0
        while r>=l:
            m = (l+r)//2
            
            if predicate(m):
                ans = m
                r = m-1
            else:
                l = m+1
        return ans