# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.iterative(root)
    
    
    def recursive(self, root):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        def preorder(root):
            nonlocal lst
            
            if not root:
                return
            
            lst.append(root.val)
            preorder(root.left)
            preorder(root.right)
            
        lst = []
        preorder(root)
        return lst
    
    def iterative(self, root):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        stk = [root]
        ret = []
        
        while stk:
            top = stk.pop()
            
            if not top:
                continue
                
            ret.append(top.val)
            
            if top.right:
                stk.append(top.right)
                
            if top.left:
                stk.append(top.left)
                
        return ret
    