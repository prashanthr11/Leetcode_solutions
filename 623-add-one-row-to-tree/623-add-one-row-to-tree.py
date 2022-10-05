# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        ret = self.bfs(root, val, depth)
        return ret

    
    def bfs(self, root, val, depth):
        if depth == 1:
            return TreeNode(val, root)
        
        queue = deque([[root, None, 1]])
        
        while queue:
            node, parent, node_depth = queue.popleft()
            
            if node_depth + 1 == depth:
                if node.left:
                    tmp = node.left
                    node.left = TreeNode(val, tmp)
                else:
                    node.left = TreeNode(val)
                    
                if node.right:
                    tmp_rt = node.right
                    node.right = TreeNode(val, None, tmp_rt)
                else:
                    node.right = TreeNode(val)
            else:
                if node.left:
                    queue.append([node.left, node, node_depth + 1])

                if node.right:
                    queue.append([node.right, node, node_depth + 1])
                    
        return root
    