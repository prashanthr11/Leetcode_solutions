class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        
        @cache
        def solve(n):
            cnt = 0
            if n == 0:
                return 1
            
            for i in nums:
                if n - i >= 0:
                    cnt += solve(n - i)
                    
            return cnt
        
        return solve(target)
    