# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = []
        mini = float('inf')
        
        def dfs(root):
            if not root:
                return
            
            dfs(root.left)
            lst.append(root.val)
            dfs(root.right)
            
        def get_min_abs_diff(lst):
            nonlocal mini
            
            i = 1
            ln = len(lst)

            while i < ln:
                mini = min(mini, lst[i] - lst[i - 1])
                i += 1
                
            return mini
        
        dfs(root)
        return get_min_abs_diff(lst)
    