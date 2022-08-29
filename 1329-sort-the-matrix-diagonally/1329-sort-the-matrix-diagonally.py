class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        '''
        Time Complexity: O(MN LogX) where X is the min(M, N)
        Space Complexity: O(MN)
        '''
        d = collections.defaultdict(list)
        n, m = len(mat), len(mat[0])
        
        for i in range(n):
            for j in range(m):
                d[i - j].append(mat[i][j])
                
        for i in d:
            d[i].sort(reverse=True)
            
        for i in range(n):
            for j in range(m):
                mat[i][j] = d[i - j].pop()
        
        return mat
    
    
    def solve(self, i, j, n, m, mat):
        tmp_i, tmp_j = i, j
        tmp_list = []

        while tmp_i < n and tmp_j < m:
            tmp_list.append(mat[tmp_i][tmp_j])
            tmp_i += 1
            tmp_j += 1

        tmp_list.sort()

        while tmp_i - 1 >= i and tmp_j - 1 >= j:
            tmp_i -= 1
            tmp_j -= 1
            mat[tmp_i][tmp_j] = tmp_list.pop()
            
        return mat
        
        
    def naive(self, mat: List[List[int]]) -> List[List[int]]:
        n, m = len(mat), len(mat[0])
        j = m - 1
        
        while j >= 0:
            self.solve(0, j, n, m, mat)
            j -= 1
            
        i = 1
        while i < n:
            self.solve(i, 0, n, m, mat)
            i += 1
            
        return mat
    