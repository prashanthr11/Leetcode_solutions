# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class TreeNodeCustom:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        self.is_root = True


class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        d = {}
        
        for parent, child, is_left in descriptions:
            if parent not in d:
                d[parent] = TreeNodeCustom(parent)
                
            if child not in d:
                d[child] = TreeNodeCustom(child)
                
            if is_left:
                d[parent].left = d[child]
            else:
                d[parent].right = d[child]
                
            d[child].is_root = False
            
        for i in d:
            if d[i].is_root:
                return d[i]
            
        return TreeNodeCustom()
    