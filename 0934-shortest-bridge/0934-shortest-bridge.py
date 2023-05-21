class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        return self.solve(grid)
    
    def populate_sets(self, x, y, grid):
        queue = deque([(x, y)])
        visited = set()
        n = len(grid)
        
        while queue:
            x, y = queue.popleft()
            
            if (x, y) in visited:
                continue
                
            visited.add((x, y))
            for i, j in self.neighbours:
                if 0 <= i + x < n and 0 <= j + y < n and grid[i + x][j + y]:
                    queue.append((i + x, j + y))
                    
        return visited
    
    def find_islands(self, grid):
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] and (i, j) not in self.set1:
                    return self.populate_sets(i, j, grid)
        
    def solve(self, grid):
        n = len(grid)
        self.set1, self.set2 = set(), set()
        self.neighbours = [(1, 0), (0, 1), (0, -1), (-1, 0)]

        self.set1 = self.find_islands(grid)
        self.set2 = self.find_islands(grid)
        
        queue = deque([(x, y, 0) for x, y in self.set1])
        visited = set()
        
        while queue:
            x, y, cnt = queue.popleft()
            
            if (x, y) in self.set2:
                return cnt - 1
            
            if (x, y) in visited:
                continue
                
            visited.add((x, y))
            
            for i, j in self.neighbours:
                if 0 <= i + x < n and 0 <= j + y < n:
                    queue.append((i + x, j + y, cnt if (i + x, j + y) in self.set1 else cnt + 1))
        
                
    def exp(self, grid):
        ln = len(grid)
        
        def get_starting_pos():
            for i in range(ln):
                for j in range(ln):
                    if grid[i][j]:
                        return (i, j, 0)
                    
        pos = get_starting_pos()
        queue = deque([pos])
        neighbours = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        visited = set()
        
        while queue:
            x, y, cnt = queue.popleft()
            
            if (x, y) in visited:
                continue
            
            if grid[x][y] and cnt:
                return cnt
            
            visited.add((x, y))
            for i, j in neighbours:
                if 0 <= i + x < ln and 0 <= j + y < ln:
                    queue.append((i + x, j + y, cnt if grid[i + x][j + y] else cnt + 1))