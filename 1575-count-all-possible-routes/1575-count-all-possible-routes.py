class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        ln = len(locations)
        dp = {}
        diffs = defaultdict(list)
        MOD = 10**9 + 7
        
        for i in range(ln):
            for j in range(ln):
                if i != j:
                    diffs[i].append((j, abs(locations[j] - locations[i])))
                
        def dfs(idx, rem_fuel):
            ret = 0
            if idx >= ln or rem_fuel < 0:
                return 0
            
            if (idx, rem_fuel) in dp:
                return dp[(idx, rem_fuel)]
            
            if rem_fuel >= 0 and idx == finish:
                ret += 1
            
            for dest_idx, dest_fuel in diffs[idx]:
                ret += dfs(dest_idx, rem_fuel - dest_fuel)
                    
            ret %= MOD
            dp[(idx, rem_fuel)] = ret
            return ret
        
        return dfs(start, fuel) % MOD