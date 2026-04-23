class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        
        indeg = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        for u, v in prerequisites:
            indeg[v]+=1
            adj[u].append(v)

        q = deque([])
        for node in range(numCourses):
            if indeg[node] == 0:
                q.append(node)

        preReq = [set() for _ in range(numCourses)]
        while q:
            node = q.popleft()
            for ne in adj[node]:
                preReq[ne].add(node)
                preReq[ne].update(preReq[node])
                indeg[ne]-=1
                if indeg[ne]==0:
                    q.append(ne)
        
        return [
            uj in preReq[vj] for uj,vj in queries
        ]