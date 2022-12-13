class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        return self.naive(matrix)
        
    def naive(self, matrix):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        '''
        n, m = len(matrix), len(matrix[0])
        
        dp = [[float('inf')]*m for i in range(n)]
        dp[0] = matrix[0]
        
        for i in range(1, n):
            for j in range(m):
                
                left_diag = dp[i - 1][j - 1] if 0 <= j - 1 else float('inf')
                right_diag = dp[i - 1][j + 1] if m > j + 1 else float('inf')
                
                dp[i][j] = min(matrix[i][j] + left_diag,
                              matrix[i][j] + dp[i - 1][j],
                              matrix[i][j] + right_diag)
        
        return min(dp[-1])
