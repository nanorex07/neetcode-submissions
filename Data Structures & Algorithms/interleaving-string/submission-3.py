class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        m = len(s1)
        n = len(s2)
        k = len(s3)
        dp = [[False]*(len(s2)+1) for _ in range(len(s1)+1)]
        dp[0][0] = True
        if len(s1) + len(s2) != len(s3):
            return False

        for i in range(1,m+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1,n+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1] 

        print(dp)
        for i in range(1,len(s1)+1):
            for j in range(1,len(s2)+1):
                state_1 = dp[i-1][j] and s1[i-1] == s3[i-1+j]
                state_2 = dp[i][j-1] and s2[j-1] == s3[i-1+j]
                dp[i][j] = state_1 or state_2

        return dp[m][n]




"""
_aabbbbaa

 _ a a a a
_T T T F F 
bF  
bF
bF
bF



"""



        # memo = {}

        # def solve(i, j, k):
        #     if k == len(s3):
        #         return True
        #     if (i,j) in memo:
        #         return memo[(i,j)]

        #     char = s3[k]
        #     memo[(i,j)]=False
        #     if i<len(s1) and j<len(s2) and s1[i] == char and s2[j]==char:
        #         memo[(i,j)] = solve(i+1,j,k+1) or solve(i,j+1,k+1)
        #     if i<len(s1) and s1[i] == char:
        #         memo[(i,j)] = solve(i+1,j,k+1)
        #     if j<len(s2) and s2[j] == char:
        #         memo[(i,j)] = solve(i,j+1,k+1)
        #     return memo[(i,j)]
        
        # return solve(0,0,0)