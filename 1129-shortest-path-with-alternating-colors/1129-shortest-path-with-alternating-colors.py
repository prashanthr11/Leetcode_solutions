class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        
        for a, b in redEdges:
            d[a].append((b, 0))
            
        for a, b in blueEdges:
            d[a].append((b, 1))
            
        answer = [-1] * n
        visited = [[False] * 2 for i in range(n)]
        
        q = deque([(0, 0, -1)])
        visited[0][1] = visited[0][0] = True
        answer[0] = 0
        
        while q:
            node, steps, color = q.popleft()
            
            for a, b in d[node]:
                if not visited[a][b] and b != color:
                    visited[a][b] = True
                    q.append((a, steps + 1, b))
                    if answer[a] == -1:
                        answer[a] = steps + 1
                        
        return answer
    