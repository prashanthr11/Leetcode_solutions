class Solution:
    def reorganizeString(self, s: str) -> str:
        return self.test(s)
    
    def test(self, s):
        d = Counter(s)
        lst = [""] * len(s)
        
        items = sorted(d.items(), key=lambda x:-x[1])
        pos = 0
        k, v = items[0]
        
        for i in range(0, len(lst), 2):
            if v <= 0:
                pos += 1
                k, v = items[pos]
                
            lst[i] = k
            v -= 1
            
        for i in range(1, len(lst), 2):
            if v <= 0:
                pos += 1
                k, v = items[pos]
                
            lst[i] = k
            v -= 1
            
        for i in range(1, len(lst)):
            if lst[i] == lst[i - 1]:
                return ""
            
        return "".join(lst)
        
        
    def naive(self, s):
        n = len(s)
        s = list(s)
        
        @cache
        def solve(idx, prev, go_back=False):            
            if idx >= n or idx < 0:
                return True
            
            if s[idx] != prev:
                return solve(idx + (1 if not go_back else -1), s[idx])
            else:
                if idx - 2 >= 0 and s[idx] != s[idx - 2]:
                    s[idx - 1], s[idx - 2] = s[idx - 2], s[idx - 1]
                    ans = solve(idx - 2, s[idx - 1], True) and solve(idx, s[idx - 1])

                    if ans:
                        return True

                    s[idx - 1], s[idx - 2] = s[idx - 2], s[idx - 1]

                if idx + 1 < n and s[idx] != s[idx + 1]:
                    s[idx], s[idx + 1] = s[idx + 1], s[idx]
                    return solve(idx + 1, s[idx])
                
                return False
            
        ans = solve(1, s[0])
        return "".join(s) if ans else ""
'''
b a a

1 b
2 a

a a b 

'''