class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        d = defaultdict(list)
        ret = 0
        
        for a, b in roads:
            d[a].append(b)
            d[b].append(a)
            
        def dfs(root, parent):
            nonlocal ret
            
            tot = 1
            
            for cur in d[root]:
                if cur == parent:
                    continue
                    
                tot += dfs(cur, root)
                
            if root != 0:
                ret += (tot + seats - 1) // seats

            return tot
        
        dfs(0, -1)
        return ret
    