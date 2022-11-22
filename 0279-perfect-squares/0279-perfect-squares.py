class Solution:
    def numSquares(self, n: int) -> int:
        '''
        Time Complexity: O(M*N), where M is the perfect squares till N
        Space Complexity: O(N)
        '''
        lst = []
        tmp = 1
        
        while tmp * tmp <= n:
            lst.append(tmp * tmp)
            tmp += 1
                    
        return self.solve_dp(lst, n, 0)

    
    def solve_dp(self, lst, n, cnt):

        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        for i in lst:
            for j in range(i, n + 1):
                dp[j] = min(dp[j], dp[j - i] + 1)

        return dp[-1]
