class Solution:
    def shortestPathAllKeys(self, grid: List[str]) -> int:
        return self.optimise(grid)
        
    def naive(self, grid):
        m, n = len(grid), len(grid[0])
        visited = defaultdict(set)
        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        all_keys = 0
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '@':
                    r, c = i, j
                elif ord('a') <= ord(grid[i][j]) <= ord('z'):
                    all_keys += 1
                
        queue = deque([(r, c, [], 0)])
        
        while queue:
            print(queue, visited)
            x, y, keys, dist = queue.popleft()
            
            if len(keys) == all_keys:
                return dist
            
            if tuple(keys) in visited[(x, y)]:
                continue
                
            visited[(x, y)].add(tuple(keys))
            
            for i, j in neighbours:
                nx, ny = x + i, y + j
                if 0 <= nx < m and 0 <= ny < n and grid[nx][ny] != "#":
                    if grid[nx][ny] in 'ABCDEFabcdef':
                        if ord('a') <= ord(grid[nx][ny]) <= ord('z'):
                            if grid[nx][ny] in list(keys):
                                continue
                                
                            new_keys = list(keys)
                            new_keys.append(grid[nx][ny])
                            new_keys = tuple(new_keys)
                            queue.append((nx, ny, new_keys, dist + 1))
                            continue
                        else:
                            if grid[nx][ny].lower() not in list(keys):
                                continue
                                
                    queue.append((nx, ny, keys, dist + 1))
                    
        return -1
        
    def optimise(self, grid):
        m, n = len(grid), len(grid[0])
        visited = set()
        all_keys = 0
        neighbours = [(-1, 0), (1, 0), (0, 1), (0, -1)]
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == "@":
                    r, c = i, j
                elif grid[i][j] in 'abcdef':
                    all_keys = all_keys | (1 << (ord(grid[i][j]) - ord('a')))
                    
        queue = deque([(r, c, 0, 0)])

        while queue:
            # print(queue)
            x, y, keys, dist = queue.popleft()
            
            if (x, y, keys) in visited:
                continue
                
            visited.add((x, y, keys))
            
            for i, j in neighbours:
                nx, ny = i + x, j + y
                if 0 <= nx < m and 0 <= ny < n:
                    if grid[nx][ny] == "#":
                        continue
                        
                    if grid[nx][ny] in 'abcdefABCDEF':
                        if ord('a') <= ord(grid[nx][ny]) <= ord('z'):
                            tmp_key = keys | (1 << (ord(grid[nx][ny]) - ord('a')))
                            
                            if tmp_key == all_keys:
                                return dist + 1
                            
                            queue.append((nx, ny, tmp_key, dist + 1))
                            continue
                        else:
                            if keys & (1 << (ord(grid[nx][ny]) - ord('A'))) == 0:
                                continue
                    
                    queue.append((nx, ny, keys, dist + 1))
                    
        return -1
    