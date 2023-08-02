class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ln = len(nums)
        
        if ln == 1:
            return [nums]
        
        ret, lst = [], []
        visited = [0] * ln
        
        def solve(idx_x, k):
            nonlocal lst
            
            if len(lst) == k:
                ret.append(lst[:])
                return 
            
            for i in range(idx_x, ln):
                for j in range(ln):
                    if visited[j]:
                        continue
                        
                    visited[j] = True
                    lst.append(nums[j])
                    solve(i + 1, k)
                    visited[j] = False
                    lst.pop()
                    
        solve(0, ln)
        return ret
    