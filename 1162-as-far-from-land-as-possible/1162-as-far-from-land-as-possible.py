class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:
        n = len(grid)
        dq = deque([(i, j, 0) for i in range(n) for j in range(n) if grid[i][j]])
        dist = [[0] * n for i in range(n)]
        visited = [[0] * n for i in range(n)]
        neighbours = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        
        while dq:
            i, j, cost = dq.popleft()
            
            if visited[i][j]:
                continue
                
            dist[i][j] = cost
            visited[i][j] = True
            
            for x, y in neighbours:
                if 0 <= i + x < n and 0 <= j + y < n and not visited[i + x][j + y]:
                    dq.append((i + x, j + y, cost + 1))
        
        maxi = -1
        for i in range(n):
            maxi = max(maxi, max(dist[i]))
            
        return maxi if maxi != 0 else -1
    