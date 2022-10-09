# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        return self.method_1(root, k)
        
    def method_1(self, root, k):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        lst = []
        self.dfs(root, lst)
        d = Counter(lst)
        
        for i in lst:
            diff = k - i
            if i == diff:
                if d[i] > 1:
                    return True
            elif d[diff]:
                return True
            
        return False
        
    def dfs(self, root, lst):
        if not root:
            return
        
        lst.append(root.val)
        self.dfs(root.left, lst)
        self.dfs(root.right, lst)
        