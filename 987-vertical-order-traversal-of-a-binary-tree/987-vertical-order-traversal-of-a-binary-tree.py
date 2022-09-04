from collections import defaultdict

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        '''
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        '''
        self.d = {}
        self.dfs(root, 0, 0)
        ret = []
        
        for k, v in sorted(self.d.items()):
            tmp = []
            for x, y in sorted(v.items()):
                tmp += sorted(y)
            ret.append(tmp)
            
        return ret
        
        
    def dfs(self, root, childs, level):
        if not root:
            return
        
        if childs not in self.d:
            self.d[childs] = {}
        
        if level not in self.d[childs]:
            self.d[childs][level] = []
            
        self.d[childs][level].append(root.val)
        
        # self.d[childs].append({level: root.val})
        self.dfs(root.left, childs - 1, level + 1)
        self.dfs(root.right, childs + 1, level + 1)