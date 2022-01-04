class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        xor_ = self.solve(n)
        # print(n, xor_)
        return n ^ xor_
        
    def solve(self, n):
        ret = 1
        while n:
            ret <<= 1
            n >>= 1
            
        return ret - 1