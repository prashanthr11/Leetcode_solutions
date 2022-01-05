class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.ret = []
        self.d = dict()
        self.palins = dict()
        
        self.solve(s, 1, len(s), [s[0]])
        return self.ret
    
    def solve(self, s, i, ln, lst):
        
        if tuple(lst) in self.d:
            return self.d[tuple(lst)]
        
        if i >= ln:
            flag = True
            for i in lst:
                if not self.ispalin(i):
                    flag = False
                    break
                    
            if flag:
                self.ret.append([i for i in lst])
            return
        
        for x in range(i, ln):
            if not self.ispalin(lst[-1]):
                break
            res = self.solve(s, x + 1, ln, lst + [s[i:x + 1]])
            self.d[tuple(lst + [s[i:x + 1]])] = res
            
        if len(lst) >= 2:
            if not self.ispalin(lst[-2]):
                return
            
        for x in range(i, ln):
            res = self.solve(s, x + 1, ln, lst[:-1] + [lst[-1] + s[i:x + 1]])
            self.d[tuple(lst[:-1] + [lst[-1] + s[i:x + 1]])] = res

    def ispalin(self, s):
        if s in self.palins:
            return self.palins[s]
        
        if len(s) == 1:
            self.palins[s] = True
            return True
        
        i, ln = 0, len(s) - 1
        while i < ln and s[i] == s[ln]:
            i += 1
            ln -= 1
            
        self.palins[s] = i >= ln
        return i >= ln
    