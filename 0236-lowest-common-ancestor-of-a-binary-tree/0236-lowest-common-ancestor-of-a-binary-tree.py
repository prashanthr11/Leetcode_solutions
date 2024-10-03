# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        parents = {}
        
        def dfs(root, parent):
            nonlocal parents
            
            if not root:
                return
            
            parents[root] = parent
            dfs(root.left, root)
            dfs(root.right, root)
            
        dfs(root, None)
        
        p_copy, q_copy = p, q
        while p_copy != q_copy:
            q_copy = parents[q_copy] if q_copy in parents else p
            p_copy = parents[p_copy] if p_copy in parents else q
            
        return p_copy
    