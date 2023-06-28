class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        d = defaultdict(list)
        
        for i in range(len(edges)):
            u, v = edges[i]
            prob = succProb[i]
            d[u].append((v, prob))
            d[v].append((u, prob))
            
        res = float('-inf')
        pq = [(-1, start)]
        visited = set()
        
        while pq:
            prob, top = heappop(pq)
            prob = -prob
            
            if top in visited:
                continue
                
            if top == end:
                res = max(res, prob)
                
            visited.add(top)
            
            for dest, dest_prob in d[top]:
                heappush(pq, (dest_prob * -prob, dest))
                
        return res if res != float('-inf') else 0
    