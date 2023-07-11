# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        def get_ref(root):
            if not root:
                return None
            
            if root == target:
                return root
            
            return get_ref(root.left) or get_ref(root.right)
        
        def make_parents(root, parent=None):
            if not root:
                return
            
            root.parent = parent
            make_parents(root.left, root)
            make_parents(root.right, root)
            
        target_node = get_ref(root)
        make_parents(root)
        queue = deque([(target_node, 0)])
        ret = []
        visited = set()
        
        while queue:
            node, level = queue.popleft()
            
            if node in visited:
                continue
            
            visited.add(node)
            if level == k:
                ret.append(node.val)
                continue
                
            if node.parent and node.parent not in visited:
                queue.append((node.parent, level + 1))
                
            if node.left and node.left not in visited:
                queue.append((node.left, level + 1))
                
            if node.right and node.right not in visited:
                queue.append((node.right, level + 1))
                
        return ret
