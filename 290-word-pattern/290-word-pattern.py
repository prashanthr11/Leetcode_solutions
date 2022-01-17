class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        front, back = dict(), dict()
        s = s.split()
        pattern_ln = len(pattern)
        if pattern_ln != len(s):
            return False
        
        for i in range(pattern_ln):
            if pattern[i] in front:
                if front[pattern[i]] != s[i]:
                    return False
            else:
                front[pattern[i]] = s[i]
                
            if s[i] in back:
                if back[s[i]] != pattern[i]:
                    return False
            else:
                back[s[i]] = pattern[i]
                
        return True
    