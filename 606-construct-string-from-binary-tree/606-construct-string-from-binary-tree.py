# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        return self.iterative(root)
    
    def recursive(self, root):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        if not root:
            return ""
        
        st = str(root.val)
        if not root.left and not root.right:
            return st
        
        if not root.right:
            return st + "(" + self.tree2str(root.left) + ")"
        
        return st + "(" + self.tree2str(root.left) + ")(" + self.tree2str(root.right) + ")"
    
    
    def iterative(self, root):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        ret = []
        stack = [root]
        visited = set()
        
        while stack:
            top = stack[-1]
            
            if top in visited:
                ret.append(")")
                stack.pop()
            else:
                visited.add(top)
                ret.append("(" + str(top.val))
                
                if not top.left and top.right:
                    ret.append("()")
                
                if top.right:
                    stack.append(top.right)
                        
                if top.left:
                    stack.append(top.left)
                    
        return "".join(ret)[1:-1]
    