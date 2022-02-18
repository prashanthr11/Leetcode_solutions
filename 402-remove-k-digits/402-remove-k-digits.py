class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stk = []
        ln = len(num)

        for i in range(ln):
            while stk and stk[-1] > int(num[i]) and k > 0:
                stk.pop()
                k -= 1
                
            if k == 0:
                return self.remove_starting_zeros(''.join([str(i) for i in stk]) + num[i:])
            
            stk.append(int(num[i]))
            
        return self.remove_starting_zeros(''.join([str(i) for i in stk[:-k]]))
    
    def remove_starting_zeros(self, s):
        for i in range(len(s)):
            if s[i] != '0':
                return s[i:]
            
        return '0'
