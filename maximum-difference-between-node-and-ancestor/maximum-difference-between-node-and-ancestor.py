# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.solve(root, root.val, root.val)
        
    def solve(self, root, mini, maxi):
        if not root:
            return maxi - mini
        
        maxi = max(maxi, root.val)
        mini = min(mini, root.val)
        
        return max(self.solve(root.left, mini, maxi), self.solve(root.right, mini, maxi))