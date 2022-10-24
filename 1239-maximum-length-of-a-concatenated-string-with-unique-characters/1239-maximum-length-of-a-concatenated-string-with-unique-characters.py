class Solution:
    def maxLength(self, arr: List[str]) -> int:

        l = []
        
        for i in arr:
            ans = self.check(i)
            if ans != False:
                l.append(ans)
        
        self.l = l
        self.memo = {}
        return self.solve(0, len(l), 0)
    
    
    def solve(self, i, ln, lst):
        if i >= ln:
            return self.calculate(lst)
        
        if (i, lst) in self.memo:
            return self.memo[(i, lst)]
        
        maxi = 0
        ret = self.are_unique(lst, self.l[i])
        if ret != False:
            maxi = self.solve(i + 1, ln, ret)
            
        maxi = max(maxi, self.solve(i + 1, ln, lst))
        self.memo[(i, lst)] = maxi
        return maxi
    
    def calculate(self, lst):
        cnt = 0
        while lst:
            cnt += (lst & 1) == 1
            lst >>= 1
            
        return cnt
        
    def are_unique(self, a, b):
        ret = a | b
        while a and b: 
            a_bit = a & 1
            b_bit = b & 1
            
            if a_bit and b_bit:
                return False
            
            a >>= 1
            b >>= 1
        
        return ret
    
    def check(self, i):
        n = 0
        
        for a in i:
            char = ord(a) - ord('a')
            if (1 << char) & n:
                return False
            
            n |= (1 << char)
            
        return n
    