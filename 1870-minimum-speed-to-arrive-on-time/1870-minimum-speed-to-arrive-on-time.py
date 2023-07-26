class Solution:
    def minSpeedOnTime(self, dist: List[int], hour: float) -> int:
        low, high = 1, 10**7
        ln = len(dist)
        
        def solve(n):
            cnt = 0
            
            for i, a in enumerate(dist):
                
                if cnt > hour:
                    break
                
                if i + 1 != ln:
                    cnt += ceil(a / n)
                else:
                    cnt += (a / n)
                    
            return cnt > hour
        
        while low < high:
            # print(low, high)
            mid = low + (high - low) // 2
            
            if solve(mid) == False:
                high = mid
            else:
                low = mid + 1
                
        res = solve(low)
        # print(low, res)
        return -1 if res else low
            