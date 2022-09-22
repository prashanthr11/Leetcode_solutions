class Solution:
    def reverseWords(self, s: str) -> str:
        return self.optimise(s)
    
    def optimise(self, s):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        ln = len(s)
        ret = [" "] * ln
        
        i, pos = 0, 0
        
        while i < ln:
            j = i
            while j < ln and s[j] != " ":
                j += 1
                
            tmp = j - 1
            while tmp >= i:
                ret[pos] = s[tmp]
                pos += 1
                tmp -= 1
                
            i = j + 1
            pos += 1
            
        return "".join(ret)
    
            