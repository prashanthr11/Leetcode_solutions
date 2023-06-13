class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        return self.naive(grid)
    
    
    def naive(self, grid):
        cnt = 0
        
        def solve(l):
            n = len(grid)
            i = 0
            ret = 0
            
            while i < n:
                j = 0
                while j < n and grid[j][i] == l[j]:
                    j += 1
                    
                i += 1
                ret += (j == n)
                
            return ret
        
        for i in grid:
            cnt += solve(i)
            
        return cnt
    