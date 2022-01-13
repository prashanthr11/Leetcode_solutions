class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key=lambda x: (x[0], x[1]))
        
        ret = 0
        maxi, mini = points[0]
        
        for start, end in points:
            if maxi <= start <= mini:
                maxi = max(maxi, start)
                mini = min(mini, end)
            else:
                ret += 1
                maxi, mini = start, end
                   
        return ret + 1
    