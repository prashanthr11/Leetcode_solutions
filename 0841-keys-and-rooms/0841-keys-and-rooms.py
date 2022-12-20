class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        return self.dfs(rooms)
    
    
    def dfs(self, rooms):
        '''
        Time Complexity: O(N + E)
        Space Complexity: O(N)
        '''
        visited = set()
        
        dq = deque([0])
        
        while dq:
            top = dq.popleft()
            
            if top in visited:
                continue
                
            visited.add(top)
            
            for neighbours in rooms[top]:
                if neighbours not in visited:
                    dq.append(neighbours)
                
        return len(visited) == len(rooms)