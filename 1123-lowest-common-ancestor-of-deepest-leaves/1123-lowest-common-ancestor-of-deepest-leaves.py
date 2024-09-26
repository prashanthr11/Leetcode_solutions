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
                    
        ancestors = self.get_ancestors(last_level[0][0], parents)
        
        for i in range(1, len(last_level)):
            tmp = last_level[i][0]
            
            while tmp and tmp not in ancestors:
                tmp = parents[tmp]
                
            while ancestors and ancestors[-1] != tmp:
                ancestors.pop()
                
        return ancestors[-1]
    
        
    def get_ancestors(self, node, parents):
        ancestors = deque([])
        
        while node and node in parents:
            ancestors.appendleft(node)
            node = parents[node]
            
        return ancestors
    