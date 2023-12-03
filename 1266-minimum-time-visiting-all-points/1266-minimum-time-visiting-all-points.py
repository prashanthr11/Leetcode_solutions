class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        return self.optimise(points)
    
    def optimise(self, points):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        total_time = 0
                
        for i in range(1, len(points)):
            x1, y1 = points[i - 1]
            x2, y2 = points[i]            
            total_time += max(abs(x2 - x1), abs(y2 - y1))
            
        return total_time
                
                
        
    def naive(self, points):
        '''
        Time Complexity: O(N * ?) - Exponential
        Space Complexity: O(8^N)
        '''
        def solve(start, end):
            queue = deque([(start[0], start[1], 0)])
            visited = set()
            
            while queue:
                x, y, cnt = queue.popleft()
                
                if (x, y) in visited:
                    continue
                    
                visited.add((x, y))
                
                if [x, y] == end:
                    return cnt
                
                queue.append((x + 1, y, cnt + 1))
                queue.append((x - 1, y, cnt + 1))
                queue.append((x, y + 1, cnt + 1))
                queue.append((x, y - 1, cnt + 1))
                queue.append((x + 1, y + 1, cnt + 1))
                queue.append((x - 1, y - 1, cnt + 1))
                queue.append((x + 1, y - 1, cnt + 1))
                queue.append((x - 1, y + 1, cnt + 1))

        total_time = 0
        
        for i in range(1, len(points)):
            total_time += solve(points[i - 1], points[i])
            
        return total_time
    