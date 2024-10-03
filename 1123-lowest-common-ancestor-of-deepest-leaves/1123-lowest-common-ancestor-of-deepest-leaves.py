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
                    
        return self.lca(root, last_level[0][0], last_level[-1][0], parents)
    
    
    def lca(self, root, p, q, parents):
        
        while p != q:
            p = parents[p] if p in parents else q
            q = parents[q] if q in parents else p
            
        return p
    