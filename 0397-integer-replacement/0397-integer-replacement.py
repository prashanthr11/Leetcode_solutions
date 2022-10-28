class Solution:
    def integerReplacement(self, n: int, cnt=0) -> int:
        self.memo = {}
        return self.solve(n, cnt)
        
    def solve(self, n, cnt):
        if n == 1:
            return cnt
        
        if n in self.memo:
            return self.memo[n]
        
        if n % 2:
            mini = min(self.integerReplacement(n + 1, cnt + 1), self.integerReplacement(n - 1, cnt + 1))
        else:
            if n & (n - 1):
                mini = self.integerReplacement(n // 2, cnt + 1)
            else:
                mini = cnt + int(math.log(n, 2))
        
        self.memo[n] = mini
        return mini