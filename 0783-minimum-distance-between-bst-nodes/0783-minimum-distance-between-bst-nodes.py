# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        lst = []
        mini = float('inf')
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            lst.append(root.val)
            dfs(root.right)
            
        dfs(root)
        i, ln = 0, len(lst)
        
        while i + 1 < ln:
            mini = min(mini, lst[i + 1] - lst[i])
            i += 1
            
        return mini
    