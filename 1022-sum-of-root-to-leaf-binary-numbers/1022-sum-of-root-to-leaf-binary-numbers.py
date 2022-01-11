# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        ret = 0
        def solve(root, value):
            if root.left is None and root.right is None:
                nonlocal ret
                ret += int(value + str(root.val), 2)
                return

            if root.left:
                solve(root.left, value + str(root.val))

            if root.right:
                solve(root.right, value + str(root.val))
                
        solve(root, '')
        
        return ret
    