class Solution:
    def trap(self, height: List[int]) -> int:
        return self.solve(height)
    
        left, right = 0, len(height) - 1
        maxL, maxR = height[left], height[right]
        result = 0
        
        while left < right:
            if maxL < maxR:
                result += maxL - height[left]
                left += 1
                maxL = max(maxL, height[left])
            else:
                result += maxR - height[right]
                right -= 1
                maxR = max(maxR, height[right])
                
        return result
        
        
    def solve(self, height):
        n = len(height)
        max_left = [height[0]] * n
        max_right = [height[-1]] * n
        
        for i in range(1, n):
            max_left[i] = max(max_left[i - 1], height[i])
            
        for i in range(n - 2, -1, -1):
            max_right[i] = max(max_right[i + 1], height[i])
            
        return sum(min(max_left[i], max_right[i]) - height[i] for i in range(n))
    
    