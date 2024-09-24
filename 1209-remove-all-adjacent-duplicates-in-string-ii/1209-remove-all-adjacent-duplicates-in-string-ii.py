class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stk = []
        
        for i in s:                
            if stk and stk[-1][0] == i:
                stk[-1][1] += 1
            else:
                stk.append([i, 1])
                
            while stk and stk[-1][1] == k:
                stk.pop()
            
        ret = ""
        
        for char, cnt in stk:
            ret += (char * cnt)
            
        return ret
