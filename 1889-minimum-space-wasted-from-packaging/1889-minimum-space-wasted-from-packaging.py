class Solution:
    def minWastedSpace(self, packages: List[int], boxes: List[List[int]]) -> int:
        return self.naive(packages, boxes)
    
    
    def naive(self, packages, boxes):
        mini = float('inf')
        MOD = 10**9 + 7
        packages.sort()
        packages_sum = sum(packages)
        
        def solve(lst):
            lst.sort()
            
            if lst[-1] < packages[-1]:
                return float('inf')
            
            prev_idx = 0
            total = 0
            
            for dim in lst:
                idx = bisect_right(packages, dim)
                total += (idx - prev_idx) * dim
                
                if idx >= len(packages):
                    break
                    
                prev_idx = idx
                
            return total - packages_sum
            
                
        for box in boxes:
            mini = min(mini, solve(box))
                
        return mini % MOD if mini != float('inf') else -1
    