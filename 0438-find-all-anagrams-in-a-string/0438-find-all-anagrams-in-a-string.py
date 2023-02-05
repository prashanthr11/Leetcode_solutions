class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return self.optimise(s, p)
    
    def optimise(self, s, p):
        
        def check(a, b):
            diff = 0
            for i in range(26):
                diff += abs(b[i] - a[i])
                
            return diff == 0
        
        ln_s, ln_p = len(s), len(p)
        d_p, d_s = [0] * 26, [0] * 26
        
        for i in p:
            d_p[ord(i) - ord('a')] += 1
            
        for i in s[:ln_p]:
            d_s[ord(i) - ord('a')] += 1
            
        ret = []
        if check(d_s, d_p):
            ret.append(0)

        for i in range(ln_p, ln_s):
            d_s[ord(s[i]) - ord('a')] += 1
            d_s[ord(s[i - ln_p]) - ord('a')] -= 1
            
            if check(d_s, d_p):
                ret.append(i - ln_p + 1)
            
        return ret
    