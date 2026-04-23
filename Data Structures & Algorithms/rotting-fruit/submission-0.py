class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        dirs = [[0,1], [0,-1], [1,0], [-1, 0]]

        q = deque([])
        fr = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    fr += 1
                if grid[i][j] == 2:
                    q.append((i,j))
        ans = 0
        while q:
            for _ in range(len(q)):
                ci, cj = q.popleft()
                for dx, dy in dirs:
                    ni, nj = ci+dx, cj+dy
                    if ni >= 0 and ni < n and nj >= 0 and nj < m and grid[ni][nj] == 1:
                        grid[ni][nj]=2
                        q.append((ni,nj))
                        fr -= 1
            if q:
                ans+=1

        return ans if fr == 0 else -1
            

