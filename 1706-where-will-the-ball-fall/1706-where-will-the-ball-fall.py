class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        n, m = len(grid), len(grid[0])
        ret = set()
        lst = [-1] * m
        dq = deque([(0, i, i) for i in range(m)])
        
        while dq:
            i, j, ball_idx = dq.popleft()
            
            if i == n:
                lst[ball_idx] = j
                continue
                
            if grid[i][j] == 1:
                if j + 1 < m and grid[i][j + 1] == 1:
                    dq.append((i + 1, j + 1, ball_idx))
            else:
                if j - 1 >= 0 and grid[i][j - 1] == -1:
                    dq.append((i + 1, j - 1, ball_idx))
            
        return lst
    