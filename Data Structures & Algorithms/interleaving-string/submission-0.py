class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        
        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def solve(i, j, k):
            if k == len(s3):
                return True
            if (i,j) in memo:
                return memo[(i,j)]

            char = s3[k]
            memo[(i,j)]=False
            if i<len(s1) and j<len(s2) and s1[i] == char and s2[j]==char:
                memo[(i,j)] = solve(i+1,j,k+1) or solve(i,j+1,k+1)
            if i<len(s1) and s1[i] == char:
                memo[(i,j)] = solve(i+1,j,k+1)
            if j<len(s2) and s2[j] == char:
                memo[(i,j)] = solve(i,j+1,k+1)
            return memo[(i,j)]
        
        return solve(0,0,0)