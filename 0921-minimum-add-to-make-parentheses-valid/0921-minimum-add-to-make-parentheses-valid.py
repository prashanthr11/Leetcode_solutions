class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        return self.optimise(s)
    
    
    def naive(self, s):
        '''
        TC: O(N)
        SC: O(N)
        '''
        stk = []
        cnt = 0
        
        for i in s:
            if i == ')':
                if stk:
                    stk.pop()
                else:
                    cnt += 1
            else:
                stk.append('(')
                
        return cnt + len(stk)
    
    
    def optimise(self, s):
        cnt, bal = 0, 0
        
        for i in s:
            bal += 1 if i == "(" else -1
            
            if bal == -1:
                cnt += 1
                bal += 1
                
        return cnt + bal
    