class Solution:
    def maximalNetworkRank(self, n: int, roads: List[List[int]]) -> int:
        d = defaultdict(list)
        
        for u, v in roads:
            d[u].append(v)
            d[v].append(u)
            
            
        def solve(x, y):
            visited = set()
            
            for i in d[x]:
                visited.add((x, i))
                
            for i in d[y]:
                if (i, y) not in visited and (y, i) not in visited:
                    visited.add((i, y))
                    
            return len(visited)
                
        maxi = 0
        for i in range(n):
            for j in range(i + 1, n):
                maxi = max(maxi, solve(i, j))
                
        return maxi