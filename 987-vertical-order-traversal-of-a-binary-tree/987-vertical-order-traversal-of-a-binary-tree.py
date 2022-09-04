# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.d = defaultdict(list)
        self.dfs(root, 0, 0)
        ret = []
        
        for k, v in sorted(self.d.items()):
            ret.append([i[1] for i in sorted(v)])
            
        return ret
    
    
    def dfs(self, root, ht, cnt):
        if not root:
            return
        
        self.d[cnt].append((ht, root.val))
        self.dfs(root.left, ht + 1, cnt - 1)
        self.dfs(root.right, ht + 1, cnt + 1)
        