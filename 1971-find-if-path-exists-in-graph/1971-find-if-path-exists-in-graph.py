class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        visited = set()
        d = defaultdict(list)
        
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
            
        dq = deque([source])
        
        while dq:
            new_source = dq.popleft()
            
            if new_source in visited:
                continue
            
            if new_source == destination:
                return True
            
            visited.add(new_source)
            
            for paths in d[new_source]:
                dq.append(paths)
                
        return False
    