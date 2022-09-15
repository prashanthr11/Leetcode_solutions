class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ln = len(s)
        spaces_ln = len(spaces)
        ret = [""] * (ln + spaces_ln)
        j = pos = 0
        
        for i in range(ln):
            if j < spaces_ln and spaces[j] == i:
                ret[pos] = " "
                j += 1
                pos += 1
                
            ret[pos] = s[i]
            pos += 1
                
            
        return "".join(ret)

    