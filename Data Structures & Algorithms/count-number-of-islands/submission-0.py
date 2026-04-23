class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n = len(grid)
        m = len(grid[0])
        dx, dy = [0,0,-1,1],[1,-1,0,0]
        
        def dfs(i: int, j: int):
            grid[i][j] = '2'
            for x in range(4):
                ni, nj = i + dx[x], j + dy[x]
                if ni >= 0 and ni < n and nj >= 0 and nj < m and grid[ni][nj]=='1':
                    dfs(ni,nj)

        
        comp = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == '1':
                    dfs(i,j)
                    comp+=1
        
        return comp



