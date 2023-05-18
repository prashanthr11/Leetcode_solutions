class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        def dfs(node, d, visited):
            for x in d[node]:
                if not visited[x]:
                    visited[x] = True
                    dfs(x, d, visited)
                    
        in_degree = [0] * n
        visited = [False] * n
        d = defaultdict(list)
        
        for u, v in edges:
            d[u].append(v)
            in_degree[v] += 1
            
        queue = deque([i for i in range(n) if in_degree[i] == 0])
        ret = []
        while queue:
            top = queue.popleft()
            
            if visited[top]:
                continue
                
            visited[top] = True
            ret.append(top)
            dfs(top, d, visited)
    
        return ret + [i for i in range(n) if not visited[i]]
    