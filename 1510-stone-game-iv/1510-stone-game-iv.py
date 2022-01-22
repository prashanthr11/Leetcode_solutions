class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        dp = [0] * (n + 1)
        dp[0] = 'A'
        squares = []
        for i in range(1, int(sqrt(n)) + 1):
            res = i * i
            squares.append(res)
            
        pos = 0
        for i in range(1, n + 1):
            if i in squares:
                dp[i] = 'A'
                pos += 1
            else:
                res = self.solve(squares[:pos], i, dp)
                dp[i] = 'A' if res else 'B'
                
        return dp[n] == 'A'
    
    
    def solve(self, lst, i, dp):
        flag = False
        
        for sqr in lst:
            if dp[i - sqr] == 'B':
                flag = True
                break
                
        return flag
    