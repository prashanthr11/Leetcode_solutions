# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        ret = self.dfs(root)
        if not ret:
            return None
        
        return root
    
    def dfs(self, root):
        if not root:
            return False
        
        lft = self.dfs(root.left)
        rt = self.dfs(root.right)
        
        if not lft:
            root.left = None
            
        if not rt:
            root.right = None
            
        if root.val == 1:
            lft = True
        
        return True if lft or rt else False
    