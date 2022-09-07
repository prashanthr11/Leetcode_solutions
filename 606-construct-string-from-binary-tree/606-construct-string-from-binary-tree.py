# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
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