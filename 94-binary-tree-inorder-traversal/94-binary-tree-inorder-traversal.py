# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ret = []
        cur = root
        while cur:
            if cur.left:
                pred = cur.left
                while pred.right and pred.right != cur:
                    pred = pred.right
                    
                if pred.right is None:
                    pred.right = cur
                    cur = cur.left
                else:
                    pred.right = None
                    ret.append(cur.val)
                    cur = cur.right
            else:
                ret.append(cur.val)
                cur = cur.right
        
        return ret