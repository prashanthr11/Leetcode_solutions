class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ret = []
        self.palins = dict()
        self.dfs(s, 0, len(s), [])
        
        return self.ret
    
    def ispalin(self, s):
        if s in self.palins:
            return self.palins[s]
        
        low, high = 0, len(s) - 1
        
        while low < high and s[low] == s[high]:
            low += 1
            high -= 1
            
        self.palins[s] = low >= high
        return low >= high
    
    def dfs(self, s, start, end, path):
        if start >= end:
            self.ret.append([i for i in path])
            return
        
        for i in range(start, end):
            if self.ispalin(s[start:i + 1]):
                self.dfs(s, i + 1, end, path + [s[start:i + 1]])