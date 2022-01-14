from string import digits as dig

class Solution:
    def myAtoi(self, s: str) -> int:
    
        i, ln = 0, len(s)
        ret = 0
        isPossitive = None
        
        while i < ln and s[i] == ' ':
            i += 1
                
        if i == ln:
            return ret
        
        if s[i] not in dig and s[i] not in '-+':
            return ret
        
        if s[i] == '+':
            isPossitive = True
            i += 1
        elif s[i] == '-':
            isPossitive = False
            i += 1
        
        j = i
        while j < ln and s[j].isdigit():
            ret = ret * 10 + ord(s[j]) - ord('0')
            j += 1
            
        if j - i:
            ret = ret if isPossitive == True or isPossitive is None else -ret
            
            if ret > 2**31 - 1:
                ret = 2**31 - 1
            elif ret < -2**31:
                ret = -2**31
            
            return ret 
        else:
            return 0
        
    