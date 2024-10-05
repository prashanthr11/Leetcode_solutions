# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        encountered_empty_node = False
        
        while queue:
            node= queue.popleft()
            
            if node.left:
                if encountered_empty_node:
                    return False
                
                queue.append(node.left)
            else:
                encountered_empty_node = True
                
            if node.right:
                if encountered_empty_node:
                    return False
                
                queue.append(node.right)
            else:
                encountered_empty_node = True
                
        return True
