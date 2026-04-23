class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        dirs = [[0,1],[0,-1],[1,0],[-1,0]]
        n, m = len(grid), len(grid[0])
        def bfs(i, j):
            area = 1
            grid[i][j] = 0
            q = deque([(i,j)])

            while q:
                ci, cj = q.popleft()
                for x, y in dirs:
                    ni, nj = ci+x, cj+y
                    if ni >= 0 and ni < n and nj >= 0 and nj < m and grid[ni][nj]==1:
                        area+=1
                        grid[ni][nj] = 0
                        q.append((ni,nj))
            return area

        ans = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    ans = max(ans, bfs(i,j))

        return ans
