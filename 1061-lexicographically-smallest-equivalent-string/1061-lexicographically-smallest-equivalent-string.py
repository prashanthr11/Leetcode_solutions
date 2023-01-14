class DSU:
    
    def __init__(self, n):
        self.parent = [i for i in range(n)]
                
    def find(self, n):
        if self.parent[n] != n:
            self.parent[n] = self.find(self.parent[n])
        
        return self.parent[n]
    
    def union(self, x, y):
        x_parent, y_parent = self.find(x), self.find(y)
        
        if x_parent > y_parent:
            x_parent, y_parent = y_parent, x_parent
            
        self.parent[y_parent] = x_parent

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        
        dsu_obj = DSU(26)
        ret = ""
        
        for i, a in enumerate(s1):
            b = ord(s2[i]) - ord('a')
            dsu_obj.union(ord(a) - ord('a'), b)
            
        for i in baseStr:
            tmp = dsu_obj.find(ord(i) - ord('a'))
            ret += chr(ord('a') + tmp)
            
        return ret
    