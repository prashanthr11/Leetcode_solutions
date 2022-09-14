# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # return self.iterative(root)
        self.cnt = 0
        self.recursive(root, 0)
        return self.cnt
    
    def recursive(self, root, value):
        if not root:
            return
        
        value ^= (1 << root.val)
        if not root.left and not root.right:
            if not value & (value - 1):
                self.cnt += 1
                
        self.recursive(root.left, value)
        self.recursive(root.right, value)
        
    
    def iterative(self, root):
        stack = [(root, 0)]
        cnt = 0
        
        while stack:
            top, value = stack.pop()
                
            value ^= (1 << top.val)
            if not top.left and not top.right:
                if value & (value - 1) == 0:
                    cnt += 1
            else:
                if top.left:
                    stack.append((top.left, value))
                
                if top.right:
                    stack.append((top.right, value))
                
        return cnt
    