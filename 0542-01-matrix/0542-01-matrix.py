class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        
        for i in range(n):
            for j in range(m):
                if mat[i][j]:
                    top = mat[i - 1][j] if i - 1 >= 0 else float('inf')
                    left = mat[i][j - 1] if j - 1 >= 0 else float('inf')
                    mat[i][j] = min(top, left) + 1
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if mat[i][j]:
                    right = mat[i][j + 1] if j + 1 < m else float('inf')
                    bottom = mat[i + 1][j] if i + 1 < n else float('inf')
                    mat[i][j] = min(mat[i][j], right + 1, bottom + 1)
                    
        return mat
    