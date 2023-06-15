# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(int)
        maxi = float('-inf')
        
        def dfs(root):
            queue = deque([(root, 1)])

            while queue:
                top_root, level = queue.popleft()
                d[level] += top_root.val

                if top_root.left:
                    queue.append((top_root.left, level + 1))

                if top_root.right:
                    queue.append((top_root.right, level + 1))
            
        dfs(root)
        
        for k, v in d.items():
            if v > maxi:
                maxi = v
                ret = k
                
        return ret
    