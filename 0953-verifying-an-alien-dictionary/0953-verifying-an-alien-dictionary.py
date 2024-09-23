class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_map = {}
        
        for i, a in enumerate(order):
            order_map[a] = i
            
        for i in range(1, len(words)):
            if not self.solve(words[i - 1], words[i], order_map):
                return False
            
        return True
    
    
    def solve(self, a, b, order):
        n, m = len(a), len(b)
        i, j = 0, 0
        
        while i < n or j < m:
            if i == n:
                return True
            
            if j == m:
                return False
            
            if order[a[i]] < order[b[j]]:
                return True
            elif order[a[i]] == order[b[j]]:
                i += 1
                j += 1
            else:
                return False
            
        return True
    