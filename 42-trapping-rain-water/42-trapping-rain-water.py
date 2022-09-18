class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        ret = i = 0
        ln = len(height)
        
        while i + 1 < ln and height[i] < height[i + 1]:
            i += 1
            
        j = ln - 1
        while j - 1 > 0 and height[j] < height[j - 1]:
            j -= 1
        
        while i <= j:
            while stack and stack[0][1] < height[i]:
                idx, cst = stack.pop()
                ret += (i - idx) * cst - sum(height[idx:i])
                
            if not stack or stack[-1][1] < height[i]:
                stack.append((i, height[i]))
                
            i += 1
        
        idx, cost = stack.pop()

        while j > idx:
            tmp = j - 1
            while tmp > idx and height[tmp] < height[j]:
                tmp -= 1
            
            ret += (j - tmp) * height[j] - sum(height[tmp + 1:j + 1])
            j = tmp
            
        return ret