# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        queue = deque([(root, 0)])
        expected_idx = 0
        
        while queue:
            node, idx = queue.popleft()
            
            if idx != expected_idx:
                return False
            
            expected_idx += 1
            if node.left:
                queue.append((node.left, 2 * idx + 1))
                
            if node.right:
                queue.append((node.right, 2 * idx + 2))
                
        return True
