class Solution:
    def maxProfit(self, k: int, prices: List[int]) -> int:
        n = len(prices)
        
        dp = [[0]*(2*k + 1) for i in range(n + 1)]
        
        
        for i in range(n - 1, -1, -1):
            for j in range(2*k - 1, -1, -1):
                if j % 2:
                    dp[i][j] = max(prices[i] + dp[i + 1][j + 1], dp[i + 1][j])
                else:
                    dp[i][j] = max(-prices[i] + dp[i + 1][j + 1], dp[i + 1][j])
                    
            
        return dp[0][0]
    