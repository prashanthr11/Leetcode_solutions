class Solution:
    def executeInstructions(self, n: int, startPos: List[int], s: str) -> List[int]:
        '''
        Time Complexity: O(M^2 + N^2)
        Space Complexity: O(1)
        '''
        ln = len(s)
        ret = [0] * ln
        
        for i in range(ln):
            ret[i] = self.solve(startPos[0], startPos[1], s[i:], n)
            
        return ret
    
    
    def solve(self, i, j, s, n):
        pos = 0
        ln = len(s)
        while i < n and j < n and i >= 0 and j >= 0 and pos < ln:
            if s[pos] == 'U':
                i -= 1
            elif s[pos] == 'D':
                i += 1
            elif s[pos] == 'L':
                j -= 1
            else:
                j += 1
            pos += 1
        
        return ln if i < n and j < n and j >= 0 \
    and i >= 0 and pos == ln else pos - 1
    