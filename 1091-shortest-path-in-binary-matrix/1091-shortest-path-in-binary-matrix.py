class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        if grid[0][0] == 1:
            return -1
        
        n = len(grid)
        queue = deque([(0, 0, 1)])
        visited = set()
        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (1, 1), (1, -1), (-1, 1)]
        
        while queue:
            x, y, steps = queue.popleft()
            
            if (x, y) in visited:
                continue
            
            if (x, y) == (n - 1, n - 1):
                return steps
            
            visited.add((x, y))
            
            for i, j in neighbours:
                if 0 <= i + x < n and 0 <= j + y < n:
                    if grid[i + x][j + y] == 0 and (i + x, j + y) not in visited:
                        queue.append((i + x, j + y, steps + 1))
                    
        return -1
    