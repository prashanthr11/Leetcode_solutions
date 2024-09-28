class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        i, n = 0, len(height) - 1
        
        while i < n:
            res =  max(res, (n - i) * min(height[i], height[n]))
            
            if height[i] <= height[n]:
                i += 1
            else:
                n -= 1
                
        return res