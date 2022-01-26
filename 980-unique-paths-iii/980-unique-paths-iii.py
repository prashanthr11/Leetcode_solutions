class Solution:
    def uniquePathsIII(self, grid: List[List[int]]) -> int:
        visited = set()
        n, m = len(grid), len(grid[0])
        
        def solve(n, m, i, j):
            if i < 0 or j < 0 or i >= n or j >= m:
                return 0
            
            if (i, j) == end:
                # print(visited)
                return self.check(visited, grid)
            
            if (i, j) in visited:
                return 0
            
            visited.add((i, j))
            sumi = 0
            sumi += solve(n, m, i + 1, j)
            sumi += solve(n, m, i, j + 1)
            sumi += solve(n, m, i - 1, j)
            sumi += solve(n, m, i, j - 1)
            visited.remove((i, j))
            
            return sumi
        
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    start = (i, j)
                elif grid[i][j] == 2:
                    end = (i, j)
                elif grid[i][j] == -1:
                    visited.add((i, j))
                    
        return solve(n, m, start[0], start[1])
        
        
        
    def check(self, vis, grid):
        return len(vis) == len(grid) * len(grid[0]) - 1
        '''
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] != 2 and (i, j) not in vis:
                    return 0
                
        return 1
        '''