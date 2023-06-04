class DSU:
    def __init__(self, n):
        self.lst = list(range(n))
        self.rank = [0] * n
        
    def find(self, n):
        if self.lst[n] != n:
            self.lst[n] = self.find(self.lst[n])

        return self.lst[n]

    def union(self, a, b):
        par_a, par_b = self.find(a), self.find(b)
        
        if self.rank[par_a] > self.rank[par_b]:
            self.lst[par_b] = par_a
        elif self.rank[par_a] < self.rank[par_b]:
            self.lst[par_a] = par_b
        else:
            self.lst[par_a] = par_b
            self.rank[par_a] += 1

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        dsu_obj = DSU(n)
        
        for i in range(n):
            for j in range(i + 1, n):
                if i != j and isConnected[i][j]:
                    dsu_obj.union(i, j)
                    
        st = set()
        for i in range(n):
            res = dsu_obj.find(i)
            
            if res not in st:
                st.add(res)
                
        return len(st)
    