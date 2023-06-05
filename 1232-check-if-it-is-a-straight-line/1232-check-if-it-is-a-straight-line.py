class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        def diff(a, b):
            return b - a
        
        x1, y1 = coordinates[0]
        x2, y2 = coordinates[1]
        
        x_diff = diff(x1, x2)
        y_diff = diff(y1, y2)
        
        for i in range(2, len(coordinates)):
            if y_diff * diff(coordinates[i - 1][0], coordinates[i][0]) != x_diff * diff(coordinates[i - 1][1], coordinates[i][1]):
                return False
            
        return True
        