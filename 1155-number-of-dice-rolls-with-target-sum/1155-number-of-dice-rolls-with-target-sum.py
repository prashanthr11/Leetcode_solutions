class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:

        self.memo = {}
        MOD = 10**9 + 7
        return self.recursive(n, k, target) % MOD
        
    def recursive(self, n, k, target):
        if n < 0 or n > target:
            return 0
        
        if (n, target) in self.memo:
            return self.memo[(n, target)]
        
        if n == 0:
            ret = 1 if target == 0 else 0
            self.memo[(n, target)] = ret
            return ret
        
        cnt = 0
        for i in range(1, k + 1):
            cnt += self.recursive(n - 1, k, target - i)
        
        self.memo[(n, target)] = cnt
        return cnt
