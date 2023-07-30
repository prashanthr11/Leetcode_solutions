class Solution:
    def integerBreak(self, n: int) -> int:
        dp = {}
        
        def solve(n, flag=False):
            if n == 0:
                return 0
            
            if n == 1:
                return 1
            
            if n in dp:
                return dp[n]
            
            maxi = 0 if flag else n
            
            for i in range(n - 1, 0, -1):
                maxi = max(maxi, i * solve(n - i))
                
            dp[n] = maxi
            return maxi
        
        return solve(n, True)