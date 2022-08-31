class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        while k:
            grid = self.shift(grid)
            k -= 1
            
        return grid
    
    
    def shift(self, grid):
        for i in range(len(grid)):
            grid[i] = [grid[i][-1]] + grid[i][:-1]

        tmp = [i[0] for i in grid]
        tmp = [tmp[-1]] + tmp[:-1]
        
        for i in range(len(grid)):
            grid[i][0] = tmp[i]
            
        return grid
    