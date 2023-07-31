class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        l1, l2 = len(s1), len(s2)
        dp = {}
        
        def solve(x, y):
            
            if x == l1 and y == l2:
                return 0
            
            if x == l1:
                dp[(x, y)] = ord(s2[y]) + solve(x, y + 1)
                return dp[(x, y)]
            
            if y == l2:
                dp[(x, y)] = ord(s1[x]) + solve(x + 1, y)
                return dp[(x, y)]
                
            if (x, y) in dp:
                return dp[(x, y)]
            
            if s1[x] == s2[y]:
                dp[(x, y)] = solve(x + 1, y + 1)
            else:
                dp[(x, y)] = min(ord(s1[x]) + solve(x + 1, y),
                      ord(s2[y]) + solve(x, y + 1))
            
            return dp[(x, y)]
        
        return solve(0, 0)
    