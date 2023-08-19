class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        cnt = 0
        ret = 0
        n = len(points)
        visited = set()
        heap = [(0, 0)]
        heapify(heap)
        dist = [float('inf')] * n
        dist[0] = 0
        
        while heap:
            tmp, idx = heappop(heap)
            
            if cnt == n:
                break
            
            if idx in visited:
                continue
                
            ret += tmp
            mini = float('inf')
            
            for j in range(n):
                if idx != j and j not in visited:
                    cost = abs(points[idx][0] - points[j][0]) + abs(points[idx][1] - points[j][1])
                    
                    if dist[j] > cost:
                        dist[j] = cost
                        heappush(heap, (cost, j))

            visited.add(idx)
            cnt += 1
            
        return ret
    
            