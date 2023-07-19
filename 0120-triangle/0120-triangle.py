class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        return self.optimise(triangle)
    
    def optimise(self, triangle):
        ln = len(triangle)
        last_row = triangle[ln - 1]
        
        for i in range(ln - 2, -1, -1):
            new_row = [0] * len(last_row)
            for j in range(i + 1):
                new_row[j] = min(triangle[i][j] + last_row[j], triangle[i][j] + last_row[j + 1])
                
            last_row = new_row
            
        return last_row[0]
        
    def naive(self, triangle):
        n = len(triangle)
        dp = {}
        
        def dfs(i, j):
            if i >= n:
                return 0
            
            if (i, j) in dp:
                return dp[(i, j)]
            
            dp[(i, j)] = triangle[i][j] + min(dfs(i + 1, j), dfs(i + 1, j + 1))
            return dp[(i, j)]
        
        return dfs(0, 0)