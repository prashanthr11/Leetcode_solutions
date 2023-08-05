# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        ret = []
        l = list(permutations(list(range(1, n + 1))))
        
        def solve(root, val):
            if not root:
                return TreeNode(val)
            
            if root.val < val:
                root.right = solve(root.right, val)
            else:
                root.left = solve(root.left, val)
                
            return root
        
        def check(tmp, ret):
            ret = [i for i in ret if i.val == tmp.val]
            
            def dfs(x, y):
                if not x or not y:
                    return x == y
                
                return x.val == y.val and dfs(x.left, y.left) and dfs(x.right, y.right)
            
            for i in ret:
                if dfs(i, tmp):
                    return False
                
            return True
        
        for i in l:
            tmp = None
            for j in i:
                tmp = solve(tmp, j)
                
            if check(tmp, ret):
                ret.append(tmp)
            
        return ret