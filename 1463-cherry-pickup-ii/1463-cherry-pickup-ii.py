class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        n, m = len(grid), len(grid[0])
        d = dict()
        
        def solve(row, col1, col2):
            if col1 >= m or col1 < 0 or col2 < 0 or col2 >= m:
                return 0

            if (row, col1, col2) in d:
                return d[(row, col1, col2)]
            
            res = grid[row][col1]
            if col1 != col2:
                res += grid[row][col2]

            maxi = 0
            if row + 1 < n:
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        maxi = max(maxi, solve(row + 1, col1 + i, col2 + j))

            res += maxi
            d[(row, col1, col2)] = res
            return res
        
        return solve(0, 0, m - 1)