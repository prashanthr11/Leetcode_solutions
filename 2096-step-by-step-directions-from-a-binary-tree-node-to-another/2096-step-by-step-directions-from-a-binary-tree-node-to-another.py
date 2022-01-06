# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        lca = self.LCA(root, startValue, destValue)
        left_s = []
        right_s = []
        
        self.get_path(lca, startValue, left_s)
        self.get_path(lca, destValue, right_s)

        return 'U' * len(left_s) + ''.join(right_s)
    
    def get_path(self, root, value, path):
        if not root:
            return False

        if root.val == value:
            return True

        path.append('L')
        res = self.get_path(root.left, value, path)
        if res:
            return True

        path.pop()
        path.append('R')
        res = self.get_path(root.right, value, path)
        if res:
            return True
        path.pop()
        return False
    
    
    def LCA(self, root, start, end):
        if not root or root.val == start or root.val == end:
            return root
        
        lft = self.LCA(root.left, start, end)
        rt = self.LCA(root.right, start, end)
        
        if lft and rt:
            return root
        
        return lft if lft else rt