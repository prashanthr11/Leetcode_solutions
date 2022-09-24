# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        return self.bfs(root, targetSum)
    
    
    def dfs(self, root, target):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        
        self.ret = []
        
        if not root:
            return self.ret
        
        self.solve(root, target, [root.val])
        
        return self.ret
    
    def solve(self, root, target, path):
        if not root or not root.left and not root.right:
            if sum(path) == target:
                self.ret.append(path[:])
            return
        
        if root.left:
            path.append(root.left.val)
            self.solve(root.left, target, path)
            path.pop()
        
        if root.right:
            path.append(root.right.val)
            self.solve(root.right, target, path)
            path.pop()
            
            
    def bfs(self, root, target):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        ret = []
        
        if not root:
            return ret
        
        queue = deque([(root.val, root, [root.val])])
        
        while queue:
            cost, first, path = queue.popleft()
            
            if not first.left and not first.right:
                if cost == target:
                    ret.append(path)
                
                continue
                
            if first.left:
                queue.append((cost + first.left.val, first.left, path + [first.left.val]))
                
            if first.right:
                queue.append((cost + first.right.val, first.right, path + [first.right.val]))
                
        return ret