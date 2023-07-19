class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        
        prev = grid[0]
        
        for i in range(n):
            next = prev
            for j in range(m):
                if i == 0:                    
                    next[j] += next[j - 1] if j - 1 >= 0 else 0
                    continue
                        
                if j == 0:
                    next[j] += grid[i][j]
                else:
                    next[j] = min(prev[j], next[j - 1]) + grid[i][j]
                    
            prev = next
            
        return prev[-1]
    