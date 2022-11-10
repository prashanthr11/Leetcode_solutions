class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        lft, ln = 0, len(costs)
        pq = []
        ret = 0
        
        while lft < candidates:
            pq.append((costs[lft], lft))
            lft += 1
            
        n = ln - 1
        while n >= ln - candidates and n >= lft:
            pq.append((costs[n], n))
            n -= 1
            
        heapify(pq)
        
        while k:
            val, idx = heappop(pq)
            ret += val
            
            if lft > n:
                k -= 1
                continue
                
            if idx < lft:
                heappush(pq, (costs[lft], lft))
                lft += 1
            else:
                heappush(pq, (costs[n], n))
                n -= 1
                
            k -= 1
            
        return ret
    