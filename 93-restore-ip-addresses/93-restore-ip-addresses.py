class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        ln = len(s)
        ret = []
        
        if ln <= 3 or ln > 12:
            return ret
        
        def solve(i, n, st, lst):
            if i > n + 1 or len(st) > 3 or len(lst) > 4:
                return False
            
            if i > n:
                if len(lst) != 4:
                    return
                
                flag = True
                for i in lst:
                    if 1 <= len(i) <= 3 and str(int(i)) == i and 0 <= int(i) <= 255:
                        continue
                    else:
                        flag = False
                        break
                        
                if flag:
                    ret.append('.'.join(lst))
                    
                return
                
            if i == n:
                solve(i + 1, n, '', lst + [st])
            else:
                solve(i + 1, n, s[i], lst + [st])
                solve(i + 1, n, st + s[i], lst)
        
        solve(0, ln, '', [])
        return ret