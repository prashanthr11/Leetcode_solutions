class Solution:
    def concatenatedBinary(self, n: int) -> int:
        return self.optimise(n)
    
    def naive(self, n):
        ret = ""
        MOD = 10**9 + 7
        
        for i in range(1, n + 1):
            ret += bin(i)[2:]
            
        return int(ret, 2) % MOD
    
    def optimise(self, n):
        binary_digits = 0
        MOD = 10**9 + 7
        ret = 0
        
        for i in range(1, n + 1):
            if i & (i - 1) == 0:
                binary_digits += 1
                
            ret = (ret << binary_digits) + i
            ret = ret % MOD
                
        return ret
    
    