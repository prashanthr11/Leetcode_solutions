# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        parents = {}
        
        dq = deque([(root, None)])
        last_level = None
        
        while dq:
            last_level = dq.copy()
            
            for i in range(len(dq)):
                node, parent_node = dq.popleft()
                
                parents[node] = parent_node
                
                if node.left:
                    dq.append((node.left, node))
                    
                if node.right:
                    dq.append((node.right, node))
                    
        return self.lca(root, last_level[0][0], last_level[-1][0])
    
    
    def lca(self, root, p, q):
        if not root:
            return None
        
        if root == p or root == q:
            return root
        
        left = self.lca(root.left, p, q)
        right = self.lca(root.right, p, q)
        return root if left and right else left or right
    