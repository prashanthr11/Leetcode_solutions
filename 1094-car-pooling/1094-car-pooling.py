class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        heap = []
        
        for pas, start, end in trips:
            heapq.heappush(heap, (end, -pas))
            heapq.heappush(heap, (start, pas))
            
        # print(heap)
        while heap:
            top = heapq.heappop(heap)
            # print(top)
            capacity -= top[1]
            if capacity < 0:
                return False
            
        return True