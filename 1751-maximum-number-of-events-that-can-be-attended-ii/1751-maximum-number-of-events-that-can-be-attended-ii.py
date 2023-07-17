class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        ln = len(events)
        starts = [start for start, _, _ in events]
        binary_searches = [bisect.bisect_right(starts, events[i][1]) for i in range(ln)]
        cache = {}
        
        def solve(idx, k):
            if idx >= ln or k == 0:
                return 0
            
            if (idx, k) in cache:
                return cache[(idx, k)]
            
            cache[(idx, k)] = max(solve(idx + 1, k), events[idx][2] + solve(binary_searches[idx], k - 1))
            
            return cache[(idx, k)]
        
        return solve(0, k)