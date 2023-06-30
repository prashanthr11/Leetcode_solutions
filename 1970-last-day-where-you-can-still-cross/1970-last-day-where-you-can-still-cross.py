class Solution:
    def latestDayToCross(self, row: int, col: int, cells: List[List[int]]) -> int:
        low, high = 1, row * col
        
        while low < high:
            mid = high - (high - low) // 2
            
            if self.solve(row, col, cells, mid):
                low = mid
            else:
                high = mid - 1
                
        return low
    
    def solve(self, row, col, lst, mid):
        grid = [[0] * col for i in range(row)]
        
        for i in range(mid):
            x, y = lst[i]
            grid[x - 1][y - 1] = 1
            
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        queue = deque([])
        for i in range(col):
            if grid[0][i] == 0:
                grid[0][i] = 1
                queue.append((0, i))
                
        while queue:
            x, y = queue.popleft()
            
            if x == row - 1:
                return True
            
            for i, j in neighbours:
                if 0 <= i + x < row and 0 <= j + y < col and grid[i + x][j + y] == 0:
                    queue.append((i + x, j + y))
                    grid[i + x][j + y] = 1
                    
        return False
    