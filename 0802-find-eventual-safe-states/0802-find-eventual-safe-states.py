class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        ln = len(graph)
        
        outorder = [0] * ln
        inorder = [0] * ln
        
        for i, a in enumerate(graph):
            for j in a:
                d[i].append(j)
                inorder[j] += 1
                outorder[i] += 1
                
        visited = [0] * ln
        terminal_nodes = set([i for i in range(ln) if outorder[i] == 0])
        
        
        def dfs(node):
            if node in terminal_nodes:
                return True
            
            if visited[node]:
                return False
            
            visited[node] = 1
            for edges in d[node]:
                res = dfs(edges)
                if res == False:
                    return res
                
            # visited[node] = 0
            terminal_nodes.add(node)
            return True
        
        for i in range(ln):
            if visited[i]:
                continue
                
            dfs(i)
            
        # res = set([i for i in range(ln) if visited[i] == 0])
        # return sorted(res.union(terminal_nodes))
        
        return sorted(terminal_nodes)
    