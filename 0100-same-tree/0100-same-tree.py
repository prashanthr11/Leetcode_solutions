# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        '''
        Time Complexity: O(N + M) where N and M are the number of nodes in p and q trees 
        Space Complexity: O(N + M)
        '''
        queue1, queue2 = [p], [q]
        
        while queue1 or queue2:
            tree1, tree2 = queue1.pop(), queue2.pop()
            
            if tree1 is None or tree2 is None:
                if tree1 != tree2:
                    return False
                else:
                    continue
                    
            if tree1.val != tree2.val:
                return False
            
            queue1.append(tree1.right)
            queue1.append(tree1.left)
            queue2.append(tree2.right)
            queue2.append(tree2.left)
                
        return True
    