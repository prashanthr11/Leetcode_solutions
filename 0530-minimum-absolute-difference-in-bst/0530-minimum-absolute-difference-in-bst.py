# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        lst = []
        mini = float('inf')
        
        def morris(root):
            cur = root
            
            while cur:
                if cur.left is None:
                    lst.append(cur.val)
                    cur = cur.right
                else:
                    tmp = cur.left
                    
                    while tmp.right and tmp.right != cur:
                        tmp = tmp.right
                        
                    if tmp.right:
                        tmp.right = None
                        lst.append(cur.val)
                        cur = cur.right
                    else:
                        tmp.right = cur
                        cur = cur.left
        
        def dfs(root):
            stk = []
            cur = root
            
            while True:
                
                if cur:
                    stk.append(cur)
                    cur = cur.left
                else:
                    if stk:
                        cur = stk.pop()
                        lst.append(cur.val)
                        cur = cur.right
                    else:
                        break
            
        def get_min_abs_diff(lst):
            nonlocal mini
            
            i = 1
            ln = len(lst)

            while i < ln:
                mini = min(mini, lst[i] - lst[i - 1])
                i += 1
                
            return mini
        
        morris(root)
        return get_min_abs_diff(lst)
    