class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        cnt = 0
        rows, cols = len(grid), len(grid[0])
        
        def get_count(r, c):
            ret = 4
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                    ret -= 1
                    
            return ret
        
        for row in range(rows):
            for col in range(cols):
                if grid[row][col]:
                    cnt += get_count(row, col)
                    
        return cnt
    