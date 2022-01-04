class Solution:
    def bitwiseComplement(self, n: int) -> int:
        bin_ = bin(n)[2:]
        ln = len(bin_)
        ret = [''] * ln
        
        for i in range(ln):
            ret[i] = '0' if bin_[i] == '1' else '1'
            
        return int(''.join(ret), 2)