class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        low, high = min(weights), sum(weights)
        
        
        def solve(n):
            container_weight = 0
            days_cnt = 0
            
            for i in weights:
                if i > n:
                    return False
                
                if container_weight + i <= n:
                    container_weight += i
                else:
                    days_cnt += 1
                    container_weight = i
                    
            days_cnt += 1 if container_weight else 0
                
            return days_cnt <= days
        
        ans = float('inf')
        while low <= high:
            mid = low + (high - low) // 2
            
            if solve(mid):
                ans = min(ans, mid)
                high = mid - 1
            else:
                low = mid + 1
                
        return ans
    