class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        return self.optimise(grid)
    
    
    def optimise(self, grid):
        r, c = -1, -1
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j]:
                    r, c = i, j
                    break
                    
        def get_count(r, c):
            lst = []
            for nr, nc in [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]:
                if 0 <= nr < len(grid) and 0 <= nc < len(grid[0]) and grid[nr][nc] == 1:
                    lst.append((nr, nc))
                    
            return lst
        
        ret = 0
        
        queue = [(r, c)]
        visited = set()
        
        while queue:
            nr, nc = queue.pop()
            
            if (nr, nc) in visited:
                continue
                
            visited.add((nr, nc))
            
            lst = get_count(nr, nc)
            queue.extend(lst)
            ret += 4 - len(lst)
            
        return ret
    