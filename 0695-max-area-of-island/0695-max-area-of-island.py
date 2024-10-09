class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        result = 0
        n, m = len(grid), len(grid[0])
        
        def solve(i, j):
            count = 0
            rows, cols = len(grid), len(grid[0])
            queue = deque([(i, j)])
            
            while queue:
                i, j = queue.popleft()
                
                if grid[i][j] == 0:
                    continue
                    
                count += 1
                grid[i][j] = 0
                
                for nr, nc in [(i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols and grid[nr][nc] == 1:
                        queue.append((nr, nc))

            return count

        for i in range(n):
            for j in range(m):
                if grid[i][j]:
                    result = max(result, solve(i, j))
                    
        return result
    