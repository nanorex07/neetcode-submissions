class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        indeg = [0]*numCourses
        adj = [[] for _ in range(numCourses)]
        for u,v in prerequisites:
            indeg[v]+=1
            adj[u].append(v)
        
        q = deque([])
        for n in range(numCourses):
            if indeg[n]==0:
                q.append(n)
        traverse = []
        while q:
            node = q.popleft()
            traverse.append(node)
            for ne in adj[node]:
                indeg[ne] -= 1
                if indeg[ne] == 0:
                    q.append(ne)
        
        return traverse[::-1] if len(traverse) == numCourses else []
                

