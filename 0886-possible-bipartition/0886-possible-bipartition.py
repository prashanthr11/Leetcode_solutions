class UnionFind:
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n
        
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
            
        return self.parent[n]
    
    def union(self, x, y):
        head_x, head_y = self.find(x), self.find(y)
        
        if head_x == head_y:
            return
        
        if self.rank[head_x] > self.rank[head_y]:
            self.parent[head_y] = head_x
        elif self.rank[head_y] > self.rank[head_x]:
            self.parent[head_x] = head_y
        else:
            self.parent[head_x] = head_y
            self.rank[head_y] += 1
            

class Solution:
    def possibleBipartition(self, n: int, dislikes: List[List[int]]) -> bool:
        edges = defaultdict(list)
        
        for u, v in dislikes:
            edges[u].append(v)
            edges[v].append(u)
            
        dsu_obj = UnionFind(n + 1)
        for u, v in edges.items():
            for i in v:
                if dsu_obj.find(u) == dsu_obj.find(i):
                    return False
                
                dsu_obj.union(i, v[0])
                
        return True
    
    