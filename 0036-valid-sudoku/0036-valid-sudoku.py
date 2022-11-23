class Solution:
    def row(self, i, j):
        return self.board[i].count(j) > 1
    
    def col(self, x, y):
        i = 0
        cnt = 0

        while i < len(self.board):
            if self.board[i][x] == y:
                cnt += 1
            i += 1
        return cnt > 1
    
    
    def submat(self, i, j, tmp):
        cnt = 0
        i, j = i*3, j*3
        
        for x in range(i, i + 3):
            for y in range(j, j + 3):
                if self.board[x][y] == tmp:
                    cnt += 1

        return cnt > 1

        
    def isValidSudoku(self, board: List[List[str]]) -> bool:    
        self.board = board
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] != '.':
                    tmp = board[i][j]
                    a, b, c = self.row(i, tmp), self.col(j, tmp), self.submat(i//3, j//3, tmp)
                    if a or b or c:
                        return False
                    
        return True