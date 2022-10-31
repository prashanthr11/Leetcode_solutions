class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        '''
        Time Complexity: O(N*M)
        Space Complexity: O(N + M)
        '''
        n, m = len(matrix), len(matrix[0])
        d = {}
        
        for i in range(n):
            for j in range(m):
                if j - i in d:
                    if d[j - i] != matrix[i][j]:
                        return False
                else:
                    d[j - i] = matrix[i][j]
                    
        return True
    