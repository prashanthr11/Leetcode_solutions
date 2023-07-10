# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        return self.bfs(root)
    
    def dfs(self, root, cnt=0):
        if not root:
            return cnt
        
        if root.left is None and root.right is None:
            return cnt + 1
        
        mini = float('inf')
        if root.left:
            mini = min(mini, self.dfs(root.left, cnt + 1))
            
        if root.right:
            mini = min(mini, self.dfs(root.right, cnt + 1))
            
        return mini
            
        
    def bfs(self, root):
        
        if not root:
            return 0
        
        queue = deque([(root, 1)])
        while queue:
            node, cnt = queue.popleft()
            
            if node.left is None and node.right is None:
                return cnt
            
            if node.left:
                queue.append((node.left, cnt + 1))
                
            if node.right:
                queue.append((node.right, cnt + 1))