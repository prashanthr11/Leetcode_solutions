class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        dt = defaultdict(dict)
        ret = []
        
        def solve(u, v, visited):
            if u not in dt or v not in dt:
                return -1
            
            if v in dt[u]:
                return dt[u][v]
            
            visited.add(u)
            for i in dt[u]:
                if i in visited:
                    continue
                    
                tmp = solve(i, v, visited)
                
                if tmp != -1:
                    return tmp * dt[u][i]
                
            return -1
        
        for i in range(len(values)):
            dt[equations[i][0]][equations[i][1]] = values[i]
            dt[equations[i][1]][equations[i][0]] = 1 / values[i]
            
        for query in queries:
            ret.append(solve(query[0], query[1], set()))
                
        return ret
    