class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # return self.naive(heights)
        return self.optimised(heights)
        
    
    def optimised(self, heights):
        stack = []
        maxi = 0
        ln = len(heights)
        
        for i in range(ln):
            # print(stack)
            while stack and heights[stack[-1]] > heights[i]:
                top = stack.pop()
                if len(stack):
                    maxi = max(maxi, heights[top] * (i - stack[-1] - 1))
                else:
                    maxi = max(maxi, heights[top] * i)
                
            stack.append(i)
            
        while stack:
            top = stack.pop()
            if len(stack):
                maxi = max(maxi, heights[top] * (ln - stack[-1] - 1))
            else:
                maxi = max(maxi, heights[top] * ln)
                
        return maxi
        
    def naive(self, heights):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        '''
        ln = len(heights)
        maxi = 0
        
        for i in range(ln):
            maxi = max(maxi, heights[i])
            for j in range(i + 1, ln):
                if heights[i] > heights[j]:
                    break
            
            maxi = max(maxi, heights[i] * (j - i))
            
        return maxi
                    