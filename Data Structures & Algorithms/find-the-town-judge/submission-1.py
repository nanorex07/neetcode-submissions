class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        
        ind, oud = [0]*(n+1), [0]*(n+1)
        for a, b in trust:
            oud[a]+=1
            ind[b]+=1
        
        found = -1
        for i in range(1, n+1):
            if oud[i] == 0 and ind[i] == n-1:
                if found != -1:
                    return found
                else:
                    found = i
        return found