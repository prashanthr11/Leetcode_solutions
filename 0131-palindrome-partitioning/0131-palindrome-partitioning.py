class Solution:
    def partition(self, s: str) -> List[List[str]]:
        ret = []
        
        def solve(i, ln, st, vis):
            if i + 1 >= ln:
                tmp = vis + [st]
                for a in tmp:
                    if a != a[::-1]:
                        return
                    
                ret.append(tmp[:])
                return
            
            solve(i + 1, ln, st + s[i + 1], vis)
            solve(i + 1, ln, s[i + 1], vis + [st])
        
        solve(0, len(s), s[0], [])
        return ret
    