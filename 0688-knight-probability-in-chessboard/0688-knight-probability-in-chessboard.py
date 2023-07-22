class Solution:
    def knightProbability(self, n: int, k: int, row: int, column: int) -> float:
        prev = [[0] * n for i in range(n)]
        neighbours = [(-2, -1), (-2, 1), (-1, -2), (-1, 2),
                     (2, -1), (2, 1), (1, -2), (1, 2)]
        
        prev[row][column] = 1
        
        for move in range(k):
            cur = [[0] * n for i in range(n)]
            
            for i in range(n):
                for j in range(n):
                    if prev[i][j] == 0:
                        continue
                        
                    for neighbour in neighbours:
                        nr, nc = i + neighbour[0], j + neighbour[1]
                        
                        if 0 <= nr < n and 0 <= nc < n:
                            cur[nr][nc] += (prev[i][j] * (1/8))
                            
            prev = cur
            
        return sum([sum(i) for i in prev])
    