class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return self.optimise(s)
    
    
    def optimise(self, s):
        n = len(s)
        lps = [0] * n
        
        i, j = 1, 0
        
        while i < n:
            if s[i] == s[j]:
                lps[i] = j + 1
                i += 1
                j += 1
            elif j != 0 and s[i] != s[j]:
                j = lps[j - 1]
            else:
                i += 1
                
        if lps[n - 1] == 0:
            return False
        
        pat = n - lps[n - 1]
        return n % pat == 0
    
        
    def naive(self, s):
        n = len(s)
        
        def solve(i, j, mod):
            while j < n:
                if s[j] != s[i]:
                    return False
                
                i += 1
                i %= mod
                j += 1
                
            return True
            
    
        
        for i in range(1, (n // 2) + 1):
            if s[i] == s[0] and n % i == 0 and solve(0, i, i):
                return True
            
        return False
    