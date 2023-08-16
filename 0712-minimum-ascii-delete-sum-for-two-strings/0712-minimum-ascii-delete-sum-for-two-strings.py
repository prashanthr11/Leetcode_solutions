class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        
        @cache
        def solve(x, y):
            sumi = 0
            
            if x >= l1 and y >= l2:
                return 0
            
            if x == l1:
                return ord(s2[y]) + solve(x, y + 1)
            
            if y == l2:
                return ord(s1[x]) + solve(x + 1, y)
            
            
            if s1[x] == s2[y]:
                return solve(x + 1, y + 1)
            else:
                return min(ord(s1[x]) + solve(x + 1, y),
                           ord(s2[y]) + solve(x, y + 1))
        
        return solve(0, 0)
    