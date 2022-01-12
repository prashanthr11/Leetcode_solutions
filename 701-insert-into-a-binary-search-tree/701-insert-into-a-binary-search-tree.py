# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        '''
        Time Complexity: O(H) where H is the height of the BST.
        Space complexity: O(H)
        Drawback: This solution doesn't gurantee a perfect balanced BST.
        '''
        def solve(root, value):
            if not root:
                return TreeNode(value)

            if root.val > value:
                root.left = solve(root.left, value)

            if root.val < value:
                root.right = solve(root.right, value)

            return root
        return solve(root, val)
    