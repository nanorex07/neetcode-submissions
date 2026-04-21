class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for a in asteroids:
            while a < 0 and stack and stack[-1]>0 and stack[-1] < -1*a:
                stack.pop()
            if not stack or stack[-1] < 0 or a > 0:
                stack.append(a)
                continue
            if stack[-1] == abs(a) and a < 0:
                stack.pop()
                continue
            if stack[-1] > abs(a):
                continue
            stack.append(a)
            

        return stack


    # -4 2