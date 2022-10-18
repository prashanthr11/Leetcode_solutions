class Solution:
    def countAndSay(self, n: int) -> str:
        '''
        Time Complexity: O(N! * m) where m is the length of the string
        Space Complexity: O(N!)
        '''
        if n == 1:
            return "1"
        
        return self.convert(self.countAndSay(n - 1))
    
    def convert(self, s):
        ln = len(s)
        i = 0
        ret = ""
        
        while i < ln:
            j = i + 1
            while j < ln and s[i] == s[j]:
                j += 1
                
            ret += str(j - i) + s[i]
            i = j
            
        return ret
    