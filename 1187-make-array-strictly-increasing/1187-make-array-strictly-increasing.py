class Solution:
    def makeArrayIncreasing(self, arr1: List[int], arr2: List[int]) -> int:
        return self.recursive(arr1, arr2)
    
        
    def recursive(self, arr1, arr2):
        arr2.sort()
        dp = dict()
        bisect_cache = dict()
        bisect_cache[-1] = arr2[bisect.bisect_right(arr2, -1)]
        
        for i in arr1 + arr2:
            idx = bisect.bisect_right(arr2, i)
            if idx < len(arr2):
                bisect_cache[i] = arr2[idx]
        
        def dfs(idx, prev):
            if idx >= len(arr1):
                return 0
            
            if (idx, prev) in dp:
                return dp[(idx, prev)]
            
            cost = float('inf')
            if arr1[idx] > prev:
                cost = dfs(idx + 1, arr1[idx])
                
            if prev in bisect_cache:
                cost = min(cost, 1 + dfs(idx + 1, bisect_cache[prev]))
            dp[(idx, prev)] = cost
            
            return cost
        
        res = dfs(0, -1)
        return res if res != float('inf') else -1
        