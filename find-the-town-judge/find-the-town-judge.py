class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        out_degree = [0] * n
        
        for a, b in trust:
            out_degree[a - 1] += 1
            
        cnt = 0
        candidate = None
        for i in range(n):
            if not out_degree[i]:
                cnt += 1
                candidate = i + 1
                
        if cnt == 1:
            vis = [False] * n
            for a, b in trust:
                if b == candidate:
                    vis[a - 1] = True
                    
                    
            for i in range(n):
                if not vis[i] and i + 1 != candidate:
                    return -1
                
            return candidate
        else:
            return -1
                