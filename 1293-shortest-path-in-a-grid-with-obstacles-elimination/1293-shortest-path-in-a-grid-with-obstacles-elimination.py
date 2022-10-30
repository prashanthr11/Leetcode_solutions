class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        dq = deque([(0, 0, k, 0)])
        n, m = len(grid), len(grid[0])
        neighbours = [(1, 0), (-1, 0), (0, -1), (0, 1)]
        mini = float('inf')
        visited = set()
        
        while dq:
            i, j, _k, cost = dq.popleft()
            if (i, j) == (n - 1, m - 1):
                mini = min(mini, cost)
                break
            
            if (i, j, _k) in visited:
                continue
                
            visited.add((i, j, _k))
            for x, y in neighbours:
                if 0 <= i + x < n and 0 <= j + y < m:
                    if grid[i + x][j + y]:
                        if _k > 0:
                            dq.append((i + x, j + y, _k - 1, cost + 1))
                    else:
                        dq.append((i + x, j + y, _k, cost + 1))
                        
        return mini if mini != float('inf') else -1