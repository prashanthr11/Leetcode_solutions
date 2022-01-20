class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def solve(l, m):
            return sum([ceil(i/m) for i in l])
        
        low, high = 1, max(piles)
        mini = high
        
        while low <= high:
            mid = (low + high) // 2
            res = solve(piles, mid)
            
            if res <= h:
                mini = min(mini, mid)
                high = mid - 1
            else:
                low = mid + 1
        
        return mini
    