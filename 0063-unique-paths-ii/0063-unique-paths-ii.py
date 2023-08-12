class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        return self.iterative(obstacleGrid)

    
    def iterative_space_optimised(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        if obstacleGrid[0][0]:
            return 0
        
        prev = [int(obstacleGrid[0][i] == 0) for i in range(n)]
        cur = prev[:]
        
        for i in range(1, m):
            for j in range(n):                    
                if obstacleGrid[i][j]:
                    cur[j] = 0
                    continue
                    
                if j != 0:
                    cur[j] = cur[j - 1] + prev[j]
            
            prev = cur
            
        return prev[n - 1]
            
        
    def iterative(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = [[0] * n for i in range(m)]
        dp[0][0] = int(obstacleGrid[0][0] == 0)
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j]:
                    continue
                
                if i == 0 and j == 0:
                    continue
                    
                if i == 0:
                    dp[i][j] = dp[i][j - 1]
                elif j == 0:
                    dp[i][j] = dp[i - 1][j]
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
                    
        return dp[m - 1][n - 1]
    
    
    def recursive(self, obstacleGrid):
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        dp = {}
        
        def solve(x, y):
            if x < 0 or y < 0:
                return 0
            
            if obstacleGrid[x][y]:
                return 0
            
            if x == 0 and y == 0:
                return 1
            
            if (x, y) in dp:
                return dp[(x, y)]
            
            dp[(x, y)] = solve(x - 1, y) + solve(x, y - 1)
            return dp[(x, y)]
        
        
        return solve(m - 1, n - 1)