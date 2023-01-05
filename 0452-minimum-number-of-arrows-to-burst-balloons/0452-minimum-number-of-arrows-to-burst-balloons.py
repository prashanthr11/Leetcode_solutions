class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        return self.naive(points)
    
    
    def naive(self, points):
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(1)
        '''
        points.sort()
        cnt = 1
        start, end = points[0]
        
        for x, y in points:
            if start <= x <= end:
                end = min(end, y)
                continue
            
            start, end = x, y
            cnt += 1
            
        return cnt