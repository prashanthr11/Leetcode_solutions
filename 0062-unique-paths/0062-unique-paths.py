class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
    
        prev = [0] * n
        cur = [0] * n
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    cur[j] = 1
                else:
                    cur[j] = cur[j - 1] + prev[j]
                    
            prev = cur
            
        return prev[n - 1]
    
        
    def naive(self, m, n):
        dp = [[0] * n for i in range(m)]
        
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    dp[i][j] = 1
                else:
                    dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
        
        return dp[m - 1][n - 1]
    