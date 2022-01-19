class Solution:
    def asteroidCollision(self, l: List[int]) -> List[int]:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        stack = list()
        ln = len(l)
        j = 0
            
        for i in range(ln):
            if l[i] >= 0:
                stack.append(l[i])
            else:
                if len(stack) == 0 or stack[-1] <= 0:
                    stack.append(l[i])
                    continue
                    
                flag = False
                while stack and stack[-1] >= 0:
                    if abs(l[i]) > stack[-1]:
                        stack.pop()
                        flag = True
                    elif abs(l[i]) < stack[-1]:
                        flag = False
                        break
                    else:
                        stack.pop()
                        flag = False
                        break
                        
                if flag:
                    stack.append(l[i])
                    
        return stack
    