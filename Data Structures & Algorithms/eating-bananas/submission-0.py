class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        def canEat(rate):
            req = 0
            for pile in piles:
                req += pile//rate + (pile%rate!=0)
            return req <= h
        
        lo, high, ans = 1, 1000000007, 0

        while high >= lo:
            mid = (high + lo) // 2

            if canEat(mid):
                ans = mid
                high = mid-1
            else:
                lo = mid+1
        return ans