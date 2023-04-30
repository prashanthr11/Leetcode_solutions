class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n
        
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
            
        return self.parent[n]
    
    def union(self, x, y):
        x_par = self.find(x)
        y_par = self.find(y)
        
        if x_par == y_par:
            return
        
        if self.rank[x_par] > self.rank[y_par]:
            self.parent[y_par] = x_par
        elif self.rank[y_par] > self.rank[x_par]:
            self.parent[x_par] = y_par
        else:
            self.parent[y_par] = x_par
            self.rank[x_par] += 1
        

class Solution:
    def distanceLimitedPathsExist(self, n: int, edgeList: List[List[int]], queries: List[List[int]]) -> List[bool]:
        return self.optimise(n, edgeList, queries)
        
    def optimise(self, n, edges, queries):
        dsu_obj = DSU(n)
        ret = [False] * len(queries)
        queries = [queries[i] + [i] for i in range(len(queries))]
        queries.sort(key=lambda x:x[2])
        edges.sort(key=lambda x:x[2])
        i = 0
        
        for u, v, lim, idx in queries:
            while i < len(edges) and edges[i][2] < lim:
                dsu_obj.union(edges[i][0], edges[i][1])
                i += 1
                
            ret[idx] = dsu_obj.find(u) == dsu_obj.find(v)
            
        return ret
    
    
    def naive(self, n, edgeList, queries):
        d = collections.defaultdict(list)
        dist = [[float('inf')]*n for i in range(n)]
        
        for u, v, dst in edgeList:
            d[u].append(v)
            d[v].append(u)
            dist[u][v] = min(dst, dist[u][v])
            dist[v][u] = min(dst, dist[v][u])
            
        ret = []
        for u, v, lim in queries:
            if self.bfs(u, v, d, dist, lim):
                ret.append(True)
            else:
                ret.append(False)
                
        return ret
    
    def bfs(self, u, v, d, dist, lim):
        queue = deque([u])
        visited = set()
        
        while queue:
            top = queue.popleft()
            
            if top in visited:
                continue
                
            if top == v:
                return True
            
            visited.add(top)
            for edge in d[top]:
                if edge not in visited and dist[top][edge] < lim and dist[edge][top] < lim:
                    queue.append(edge)
                    
        return False
    