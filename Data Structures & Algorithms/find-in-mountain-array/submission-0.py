class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:
        
        # find peak
        low = 0
        high = mountainArr.length()-1
        peak = -1
        while high >= low:
            m = (low+high)//2
            
            left = mountainArr.get(m-1)
            right = mountainArr.get(m+1)
            curr = mountainArr.get(m)

            if curr > left and curr > right:
                peak = m
                break
            
            if curr > left and curr < right:
                low = m+1
            else:
                high = m-1
        
        low = 0
        high = peak
        ans = -1
        while high >= low:
            m = (low+high)//2
            val = mountainArr.get(m)
            if val == target:
                ans = m
            if val >= target:
                high = m-1
            else:
                low = m+1
        if ans != -1:
            return ans

        low = peak+1
        high = mountainArr.length()-1
        while high >= low:
            m = (low+high)//2
            val = mountainArr.get(m)
            if val == target:
                return m
            if val < target:
                high = m-1
            else:
                low = m+1
        
        return ans
        


"""
1 2 3 4 2 1
"""