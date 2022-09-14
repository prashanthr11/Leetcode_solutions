# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        self.cnt = 0
        self.d = defaultdict(int)
        self.d[root.val] = 1
        self.dfs(root)
        return self.cnt
    
    def dfs(self, root):
        if not root:
            return
        
        if not root.left and not root.right:
            if self.palindrome_possible():
                self.cnt += 1
            return
        
        if root.left:
            self.d[root.left.val] += 1
            self.dfs(root.left)
            self.d[root.left.val] -= 1
            
        if root.right:
            self.d[root.right.val] += 1
            self.dfs(root.right)
            self.d[root.right.val] -= 1
        
    def palindrome_possible(self):
        cnt = 0
        for i in self.d:
            cnt += (self.d[i] % 2)
            
        return cnt <= 1
    