class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        peoples = (i for i, seat in enumerate(seats) if seat)
        prev, future = None, next(peoples)
        maxi = 0
        
        for i, seat in enumerate(seats):
            if seat:
                prev = i
            else:
                while future is not None and future < i:
                    future = next(peoples, None)
                    
                left = float('inf') if prev is None else i - prev
                right = float('inf') if future is None else future - i
                maxi = max(maxi, min(left, right))
                
        return maxi
    