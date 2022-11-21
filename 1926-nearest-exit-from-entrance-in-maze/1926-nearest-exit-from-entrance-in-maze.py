class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        '''
        Standard BFS
        Time Complexity: O(N*M)
        Space Complexity: O(N*M)
        '''
        queue = deque([(entrance[0], entrance[1], 0)])
        neighbours = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = set()
        
        n, m = len(maze), len(maze[0])
        while queue:
            x, y, cost = queue.popleft()
            
            if x == 0 or y == 0 or x == n - 1 or y == m - 1:
                if [x, y] != entrance:
                    return cost
                
            if (x, y) in visited:
                continue
                
            visited.add((x, y))
            for a, b in neighbours:
                if 0 <= x + a < n and 0 <= y + b < m and maze[a + x][y + b] != "+":
                    queue.append((x + a, y + b, cost + 1))
                    
        return -1
    