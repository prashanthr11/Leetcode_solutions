# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([root])
        flag = False
        
        while queue:
            for level in range(len(queue)):
                top = queue.popleft()
                
                if top is None:
                    flag = True
                    continue
                else:
                    if flag:
                        return False
                    
                    queue.append(top.left)
                    queue.append(top.right)
                    
        return flag
    