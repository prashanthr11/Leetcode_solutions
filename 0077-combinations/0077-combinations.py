class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        ret, lst = [], []
        
        def solve(j):
            nonlocal lst
            
            if len(lst) == k:
                ret.append(lst[:])
                return
            
            for i in range(j, n + 1):
                lst.append(i)
                solve(i + 1)
                lst.pop()
                
        solve(1)
        return ret
    