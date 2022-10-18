class Solution:
    def longestPalindrome(self, s: str) -> str:
        return self.optimise(s)
    
    
    def dp(self, s):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        '''
        ln = len(s)
        maxi = 1
        start = 0
        
        dp = [[0] * ln for i in range(ln)]
        
        for i in range(ln):
            dp[i][i] = 1
            
        for i in range(ln - 1):
            flag = 1 if s[i] == s[i + 1] else 0
            
            if flag:
                dp[i][i + 1] = 1
                maxi = 2
                start = i
            
        k = 3
        while k <= ln:
            i = 0
            while i < ln - k + 1:
                j = i + k - 1
                
                if dp[i + 1][j - 1] and s[i] == s[j]:
                    dp[i][j] = 1
                    
                    if k > maxi:
                        maxi = k
                        start = i
                        
                i += 1
            k += 1
            
        return s[start:start + maxi]
    
    
    def optimise(self, s):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        '''

        ln = len(s)
        maxi = start = end = 0
        
        for i in range(ln):
            inc = self.expand_center(s, i, i)
            not_inc = self.expand_center(s, i, i + 1)
            maxx = max(inc, not_inc)

            if maxx > maxi:
                maxi = maxx
                start = i - ((maxx - 1) // 2)
                end = i + (maxx // 2)
                
        return s[start: end + 1]
    
    
    def expand_center(self, s, i, j):
        ln = len(s)
        
        while i >= 0 and j < ln and s[i] == s[j]:
            i -= 1
            j += 1
            
        return j - i - 1
    