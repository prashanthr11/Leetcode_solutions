class Solution:
    def minInsertions(self, s: str) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        cnt = 0
        ln = len(s)
        i, ret = 0, 0
        
        while i < ln:
            if s[i] == '(':
                cnt += 1
            else:
                if i + 1 < ln and s[i + 1] == ')':
                    i += 1
                else:
                    ret += 1
                    
                if cnt:
                    cnt -= 1
                else:
                    ret += 1
            
            i += 1
            
        return ret + cnt * 2
    