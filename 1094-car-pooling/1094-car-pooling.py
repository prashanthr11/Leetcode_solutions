class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        trip = [0] * 1001
        
        for cap, start, end in trips:
            for i in range(start, end):
                trip[i] += cap
                if trip[i] > capacity:
                    return False
            
        return True
    