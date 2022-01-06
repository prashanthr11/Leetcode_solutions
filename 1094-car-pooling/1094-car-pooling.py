class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        trip = [0] * 1001
        
        for pas, start, end in trips:
            trip[start] += pas
            trip[end] -= pas
            
        tot = 0
        for i in trip:
            tot += i
            if tot > capacity:
                return False
            
        return True
    