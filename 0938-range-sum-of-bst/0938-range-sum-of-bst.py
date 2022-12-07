# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        return self.naive(root, low, high)
        
    
    def naive(self, root, low, high):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        
        def dfs(root, low, high):
            ret = 0
            if not root:
                return 0
            
            if low <= root.val <= high:
                ret = root.val
                
            left = dfs(root.left, low, high)
            right = dfs(root.right, low, high)
            
            return ret + left + right
        
        return dfs(root, low, high)
    