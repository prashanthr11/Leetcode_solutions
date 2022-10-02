class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        '''
        Time Complexity: O(N*M)
        Space Complexity: O(1)
        '''
        maxi = 0
        
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                neighbours = [(i, j), (i + 1, j + 1), (i + 2, j), (i, j + 1), \
                              (i, j + 2), (i + 2, j + 1), (i + 2, j + 2)]
                
                maxi = max(maxi, sum([grid[x][y] for x, y in neighbours]))
                
        return maxi
    
    