from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ret = []
        d = deque([[root]])
        
        while d:
            top = d.popleft()
            sumi = cnt = 0
            next_level = []
            
            for i in top:
                if i.left:
                    next_level.append(i.left)
                
                if i.right:
                    next_level.append(i.right)
                
                sumi += i.val
                cnt += 1
                
            ret.append(sumi/cnt)
            
            if len(next_level):
                d.append(next_level)
        
        return ret
    