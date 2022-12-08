# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def get_leaf_nodes(self, root):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        leaf_nodes = []
        
        def inorder(root):
            if not root:
                return
            
            inorder(root.left)
            
            if root.left is None and root.right is None:
                leaf_nodes.append(root.val)
                
            inorder(root.right)
            
        inorder(root)
        return leaf_nodes

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        '''
        Time Complexity: O(H1 + H2) where H1 and H2 are heights of the root1, root2 respectively
        Time Complexity: O(H1 + H2)
        '''
        return self.get_leaf_nodes(root1) == self.get_leaf_nodes(root2)
