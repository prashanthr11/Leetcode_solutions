class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        n = len(seats)
        persons = [i for i, a in enumerate(seats) if a]
        visited = [0] * n
        cnt = 0
        
        while persons:
            neighbours = []
            for persons_idx in persons:
                if persons_idx + 1 < n and not visited[persons_idx + 1]:
                    neighbours.append(persons_idx + 1)
                    visited[persons_idx + 1] = True
                    
                if persons_idx - 1 >= 0 and not visited[persons_idx - 1]:
                    neighbours.append(persons_idx - 1)
                    visited[persons_idx - 1] = True
                    
                visited[persons_idx] = True
                
            persons = neighbours
            cnt += 1
            
        return cnt - 1
    