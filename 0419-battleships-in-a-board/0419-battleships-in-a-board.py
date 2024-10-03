class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        rows, cols = len(board), len(board[0])
        
        visited = [[False] * cols for i in range(rows)]
        
        def bfs(row, col):
            queue = deque([(row, col)])
            
            while queue:
                x, y = queue.popleft()
                
                for nr, nc in [(x + 1, y), (x, y + 1)]:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if board[nr][nc] == 'X' and visited[nr][nc] == False:
                            visited[nr][nc] = True
                            queue.append((nr, nc))
                        
        
        count = 0
        for row in range(rows):
            for col in range(cols):
                if board[row][col] == "X" and visited[row][col] == False:
                    count += 1
                    bfs(row, col)
                    
        return count
    