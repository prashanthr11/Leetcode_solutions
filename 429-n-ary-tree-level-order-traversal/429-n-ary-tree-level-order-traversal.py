"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        '''
        Time Complexity: O(N Log N)
        Space Complexity: O(N)
        '''
        self.d = defaultdict(list)
        self.dfs(root)
        ret = []
        
        for k, v in sorted(self.d.items()):
            ret.append(v)
            
        return ret
    
        
    def dfs(self, root, level=0):
        if not root:
            return
        
        self.d[level].append(root.val)
        
        for i in root.children:
            self.dfs(i, level + 1)
            