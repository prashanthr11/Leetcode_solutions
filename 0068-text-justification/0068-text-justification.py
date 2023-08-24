class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        ret = []
        i = 0
        n = len(words)
        
        def solve(i):
            tmp = []
            ln = 0
            used_space = 0
            
            while i < n and used_space + ln + len(words[i]) <= maxWidth:
                tmp.append(words[i])
                used_space += len(words[i])
                ln += 1
                i += 1
                
            idx = 0
            while i < n and ln > 1 and used_space + ln - 1 < maxWidth:
                tmp[idx % (ln - 1)] += " "
                used_space += 1
                idx += 1
                
            ret = " ".join(tmp)
            ret += (" " * (maxWidth - len(ret)))
            
            return i, ret
        
        while i < n:
            i, res = solve(i)
            ret.append(res)
            
        return ret
    