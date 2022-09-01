# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ret = 0
        self.naive(root, [root.val])
        return self.ret

    
    def check(self, l):
        return len([i for i in l if i > l[-1]]) == 0
    
    
    def naive(self, root, path):
        
        if self.check(path):
            self.ret += 1
        
        if root.left:
            self.naive(root.left, path + [root.left.val])
            
        if root.right:
            self.naive(root.right, path + [root.right.val])
            