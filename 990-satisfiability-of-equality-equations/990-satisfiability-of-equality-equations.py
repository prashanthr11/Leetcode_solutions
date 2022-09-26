class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        
    def find(self, n):
        while self.parent[n] != n:
            n = self.parent[n]
            
        return self.parent[n]
    
    def union(self, a, b):
        x, y = self.find(a), self.find(b)
        self.parent[y] = x
        
        return True

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        union_find = UnionFind(26)
        flag = True
        
        for a, b, c, d in equations:
            a_ordd, d_ordd = ord(a) - ord('a'), ord(d) - ord('a')
            
            if b == "=":
                if not union_find.union(a_ordd, d_ordd):
                    return False
            
        for a, b, c, d in equations:
            if b == "!":
                a_ordd, d_ordd = ord(a) - ord('a'), ord(d) - ord('a')
                x, y = union_find.find(a_ordd), union_find.find(d_ordd)
                
                if x == y:
                    return False

        return True
    