class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        return self.dp_inplace(n, m, grid)
    
        
    def dp_inplace(self, n, m, grid):
        '''
        Time Complexity: O(N*M)
        Space Complexity: O(1)
        '''
        for i in range(n):
            for j in range(m):
                if i == 0:
                    if j != 0:
                        grid[i][j] += grid[i][j - 1]
                    continue
                    
                if j == 0:
                    grid[i][j] += grid[i - 1][j]
                else:
                    grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
                    
        # for i in grid:
        #     print(*i)
            
        return grid[-1][-1]
                        
    
    def dp_tabulation(self, n, m, grid):
        '''
        Time Complexity: O(N*M)
        Space Complexity: O(N*M)
        '''
        dp = [[float('inf')] * m for i in range(n)]
        
        for i in range(n):
            for j in range(m):
                dp[i][j] = grid[i][j]
                if i == 0:
                    dp[i][j] += dp[i][j - 1] if j != 0 else 0
                    continue
                    
                if j == 0:
                    dp[i][j] += dp[i - 1][j]
                else:
                    dp[i][j] += min(dp[i - 1][j], dp[i][j - 1])
                
        for i in dp:
            print(*i)
            
        return dp[-1][-1]
        
        
    def recursive_dp(self, i, j, grid):
        '''
        Time Complexity: O(N*M)
        Space Complexity: O(N*M)
        '''
        if i < 0 or j < 0:
            return float('inf')

        if (i, j) in self.d:
            return self.d[(i, j)]

        ret = grid[i][j]
        ret += min(self.recursive_dp(i - 1, j, grid), self.recursive_dp(i, j - 1, grid))
        self.d[(i, j)] = ret
        return ret
    