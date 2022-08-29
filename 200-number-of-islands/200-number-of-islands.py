class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        Time Complexity: O(MN)
        Space Complexity: O(MN)
        '''
        n, m = len(grid), len(grid[0])
        
        tmp_grid = [[-1]*m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                self.solve(i, j, n, m, grid, tmp_grid, (i, j))
            
        ret = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and tmp_grid[i][j] == (i, j):
                    ret += 1
                    
        return ret
    
                
    def solve(self, i, j, n, m, grid, tmp_grid, tpl):
        if tmp_grid[i][j] != -1:
            return
        
        tmp_grid[i][j] = tpl
        
        if grid[i][j] != "1":
            return
        
        for x, y in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            if 0 <= i + x < n and 0 <= j + y < m and grid[i + x][j + y] == "1":
                self.solve(i + x, j + y, n, m, grid, tmp_grid, tpl)