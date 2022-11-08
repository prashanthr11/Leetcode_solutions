class Solution:
    def makeGood(self, s: str) -> str:
        return self.optimise(s)
        
    def optimise(self, s):
        ln = len(s)
        if ln <= 1:
            return s
        
        i = 0
        stk = []
        
        while i < ln:
            while i < ln and stk and abs(ord(stk[-1]) - ord(s[i])) == 32:
                stk.pop()
                i += 1
                
            if i < ln:
                stk.append(s[i])
                
            i += 1
            
        return ''.join(stk)