# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        self.l = []
        return self.iterative(root)
    
    def recursive(self, root):
        if not root:
            return
        
        self.l.append(root.val)
        self.recursive(root.left)
        self.recursive(root.right)
        
    def iterative(self, root):
        q = [root]
        ret = []
        
        while q:
            tmp = q.pop()
            
            if not tmp:
                continue
                
            ret.append(tmp.val)
            
            if tmp.right:
                q.append(tmp.right)
                
            if tmp.left:
                q.append(tmp.left)
                
        return ret
    