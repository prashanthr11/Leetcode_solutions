class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return self.naive(s)
        
        
    def naive(self, s):
        n = len(s)
        
        def solve(i, j, mod):
            return len(s.replace(s[i:j], "")) == 0
    
        
        for i in range(1, (n // 2) + 1):
            if s[i] == s[0] and n % i == 0 and solve(0, i, i):
                return True
            
        return False
    