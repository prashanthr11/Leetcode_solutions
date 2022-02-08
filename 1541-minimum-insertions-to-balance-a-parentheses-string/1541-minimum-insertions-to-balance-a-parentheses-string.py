class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        stk = list()
        ln = len(s)
        i, ret = 0, 0
        
        while i < ln:
            if s[i] == '(':
                stk.append(s[i])
            else:
                if i + 1 < ln and s[i + 1] == ')':
                    i += 1
                else:
                    ret += 1
                    
                if stk:
                    stk.pop()
                else:
                    ret += 1
            
            i += 1
            
        return ret + len(stk) * 2
    