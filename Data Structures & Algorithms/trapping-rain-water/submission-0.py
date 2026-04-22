class Solution:
    def trap(self, height: List[int]) -> int:
        
        ans = 0
        l = 0
        r = len(height)-1
        leftMax, rightMax = height[l], height[r]
        while r > l:
            if rightMax > leftMax:
                l+=1
                leftMax = max(leftMax, height[l])
                ans += leftMax - height[l]
            else:
                r-=1
                rightMax = max(rightMax, height[r])
                ans += rightMax - height[r]
        return ans
            