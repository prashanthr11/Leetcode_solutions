class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        return self.optimise(root)
    
    def optimise(self, root):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        nodes = {}
        maxi = 0
        
        def compute_min_max(root, ht):
            nonlocal nodes
            
            if not root:
                return 10**5 + 1, 0
            
            left_min, left_max = compute_min_max(root.left, ht + 1)
            right_min, right_max = compute_min_max(root.right, ht + 1)
            nodes[(root.val, ht)] = min(left_min, right_min), max(right_max, left_max)
            
            return min(left_min, right_min, root.val), max(left_max, right_max, root.val)
            
        compute_min_max(root, 0)

        for k, v in nodes.items():
            res = v[1] - k[0]
            res = max(res, k[0] - v[0])
            maxi = max(maxi, res)
        
        return maxi

        
    def naive(self, root):
        '''
        Time Complexity: O(N * N)
        Space Complexity: O(N * N)
        '''
        maxi = 0
        queue = deque([root])
        
        while queue:
            top = queue.pop()
            
            maxi = max(maxi, self.solve(top, top.val))
            
            if top.left:
                queue.append(top.left)
                
            if top.right:
                queue.append(top.right)
                
        return maxi
    
    def solve(self, root, value):
        if not root:
            return 0
        
        return max(abs(value - root.val), self.solve(root.left, value), self.solve(root.right, value))
        