# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        Time Complexity: O(N) -> in case of slanted trees.
        Space Complexity: O(N) -> recursion stack space
        '''
        def solve(root, ht=0):
            if not root:
                return ht
            
            return max(solve(root.left, ht + 1), solve(root.right, ht + 1))
        
        if not root:
            return 0
        
        return solve(root)
    