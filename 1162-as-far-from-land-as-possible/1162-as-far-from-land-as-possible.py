class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = deque([(i, j, 0) for i in range(n) for j in range(n) if grid[i][j]])
        dist = [[0] * n for i in range(n)]
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while dq:
            i, j, cost = dq.popleft()
            
            if dist[i][j]:
                continue
                
            dist[i][j] = cost
            
            for x, y in neighbours:
                if 0 <= i + x < n and 0 <= j + y < n and grid[i + x][j + y] == 0 and dist[i + x][j + y] == 0:
                    dq.append((i + x, j + y, cost + 1))
        
        maxi = -1
        for i in range(n):
            maxi = max(maxi, max(dist[i]))
            
        return maxi if maxi != 0 else -1
    