class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ret = ""
        MOD = 10**9 + 7
        
        for i in range(1, n + 1):
            ret += bin(i)[2:]
            
        return int(ret, 2) % MOD