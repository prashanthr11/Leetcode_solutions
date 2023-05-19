class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        n = len(graph)
        visited = [False] * n
        colors = [-1] * n
        
        for i in range(n):
            if visited[i]:
                continue
                
            queue = deque([[i, False]])

            while queue:
                top, color = queue.popleft()

                if visited[top]:
                    if colors[top] == color:
                        continue
                    else:
                        return False

                visited[top] = True
                colors[top] = color
                for edge in graph[top]:
                    if colors[edge] == color:
                        return False
                    queue.append((edge, not color))

        return True
    