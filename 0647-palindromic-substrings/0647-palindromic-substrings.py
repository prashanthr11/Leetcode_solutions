class Solution:
    def countSubstrings(self, s: str) -> int:
        return self.otpimise(s)
    
    
    def otpimise(self, s):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        '''
        n = len(s)
        
        dp = [[0]*n for i in range(n)]
        
        for i in range(n):
            dp[i][i] = 1
            
        for i in range(n - 1):
            dp[i][i + 1] = int(s[i] == s[i + 1])
            
        i = 2
        while i < n:
            j = 0
            while j < n - i:
                dp[j][i + j] = int(s[j] == s[j + i] and dp[j + 1][i + j - 1])
                j += 1
                
            i += 1
            
        return sum([sum(i) for i in dp])
    
    
    def naive(self, s):
        '''
        Time Complexity: O(N^3)
        Space Complexity: O(1)
        '''
        cnt = 0
        ln = len(s)
        
        for i in range(ln):
            for j in range(i, ln):
                if self.ispalin(s[i:j + 1]):
                    cnt += 1
                    
        return cnt
    
    def ispalin(self, s):
        return s == s[::-1]
    
    '''
      a b c a
    a 1 0 0 0
    b   1 0 0
    c     1 0
    a       1
    
    '''