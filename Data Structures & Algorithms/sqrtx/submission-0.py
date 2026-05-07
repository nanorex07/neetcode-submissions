class Solution:
    def mySqrt(self, x: int) -> int:
        
        l, h = 0, x
        ans = None
        while h >= l:
            mid = l + (h-l)//2
            if mid*mid > x:
                h = mid-1
            else:
                ans = mid
                l = mid+1
        return ans