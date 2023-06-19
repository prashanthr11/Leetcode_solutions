class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        return self.recursive(grid)
    
    def recursive(self, grid):
        dp = {}
        m, n = len(grid), len(grid[0])
        MOD = 10**9 + 7
                
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        ret = 0
        
        def dfs(x, y):
            if x >= m or y >= n:
                return 0
            
            if (x, y) in dp:
                return dp[(x, y)]
            
            cnt = 1
            dp[(x, y)] = 1
            
            for x1, y1 in neighbours:
                nx, ny = x + x1, y + y1
                if 0 <= nx < m and 0 <= ny < n and grid[x][y] < grid[nx][ny]:
                    cnt += dfs(nx, ny)
                    cnt = cnt % MOD
                    
            dp[(x, y)] = cnt
            return cnt
        
        for i in range(m):
            for j in range(n):
                ret += dfs(i, j)
                ret = ret % MOD
                
        return ret % MOD
    