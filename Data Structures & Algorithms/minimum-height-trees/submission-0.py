class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adj = {
            i: [] for i in range(n)
        }

        degrees = [0]*n
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
            degrees[u]+=1
            degrees[v]+=1
        
        q = deque([])
        
        for i in range(n):
            if degrees[i]==1:
                q.append(i)
        
        while len(adj) > 2:
            for _ in range(len(q)):
                node = q.popleft()
                for ne in adj[node]:
                    degrees[ne]-=1
                    if degrees[ne] == 1:
                        q.append(ne)
                del adj[node]
        
        return list(adj.keys())

