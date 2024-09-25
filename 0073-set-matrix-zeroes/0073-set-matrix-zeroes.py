class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        return self.optimise(matrix)
    
        
    def optimise(self, matrix):
        m, n = len(matrix), len(matrix[0])
        
        def solve(x, y):
            nr, nc = 0, 0
            
            while nr < m:
                if matrix[nr][y] != 0:
                    matrix[nr][y] = float('inf')
                
                nr += 1
                
                
            while nc < n:
                if matrix[x][nc] != 0:
                    matrix[x][nc] = float('inf')
                    
                nc += 1
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    solve(i, j)
                    
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == float('inf'):
                    matrix[i][j] = 0
                    