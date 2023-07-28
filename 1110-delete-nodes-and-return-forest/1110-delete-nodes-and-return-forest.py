# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def delNodes(self, root: Optional[TreeNode], to_delete: List[int]) -> List[TreeNode]:
        if not root:
            return []
        
        d = {}
        parents = {}
        
        def set_parents(node, parent):
            nonlocal d
            
            if not node:
                return
            
            d[node.val] = node
            parents[node.val] = parent
            set_parents(node.left, node)
            set_parents(node.right, node)
        
        set_parents(root, None)
        
        is_root = set([root.val])
        
        for to_del in to_delete:
            node = d[to_del]
            parent_node = parents[node.val]
            
            if parent_node:
                if parent_node.left and parent_node.left.val == to_del:
                    parent_node.left = None
                else:
                    parent_node.right = None
                    
            if to_del in is_root:
                is_root.remove(to_del)
                
            if node.left:
                is_root.add(node.left.val)
                
            if node.right:
                is_root.add(node.right.val)
                
        ret = []
        for i in is_root:
            ret.append(d[i])
                
        return ret
    