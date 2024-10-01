class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        rows, cols = len(isWater), len(isWater[0])
        
        queue = deque([(i, j) for i in range(rows) for j in range(cols) if isWater[i][j] == 1])
        distance = 0
        
        while queue:
            distance += 1
            
            for _ in range(len(queue)):
                row, col = queue.popleft()
                    
                for i, j in [(-1, 0), (1, 0), (0, 1), (0, -1)]:
                    nr, nc = i + row, j + col
                    
                    if 0 <= nr < rows and 0 <= nc < cols and isWater[nr][nc] == 0:
                        isWater[nr][nc] = -distance
                        queue.append((nr, nc))
                        
        for row in range(rows):
            for col in range(cols):
                if isWater[row][col] == 1:
                    isWater[row][col] = 0
                else:
                    isWater[row][col] = -isWater[row][col]
                    
        return isWater
    