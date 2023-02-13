class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        
        for u, v in redEdges:
            d[u].append((v, 0))
            
        for u, v in blueEdges:
            d[u].append((v, 1))
            
        q = deque([(0, 0, -1)])
        visited = [[False] * 2 for i in range(n)]
        answer = [-1] * n
        
        while q:
            node, cost, node_color = q.popleft()
            
            if visited[node][node_color]:
                continue
                
            if node_color == -1:
                visited[node][0] = visited[node][1] = True
            else:
                visited[node][node_color] = True
                
            if answer[node] == -1:
                answer[node] = cost
            else:
                answer[node] = min(answer[node], cost)
            
            for childs, color in d[node]:
                if visited[childs][color] == False and color != node_color:
                    q.append((childs, cost + 1, color))
                    
        return answer
    