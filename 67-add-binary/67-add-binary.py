class Solution:
    def addBinary(self, a: str, b: str) -> str:
        a_ln, b_ln = len(a), len(b)
        
        if a_ln > b_ln:
            b = '0' * (a_ln - b_ln) + b
        elif a_ln < b_ln:
            a = '0' * (b_ln - a_ln) + a
            
        carry = 0
        ret = ''
        ln = len(a) - 1
        
        while ln >= 0:
            if a[ln] == b[ln]:
                if a[ln] == '1':
                    if carry:
                        ret = '1' + ret
                    else:
                        carry = 1
                        ret = '0' + ret
                else:
                    if carry:
                        carry = 0
                        ret = '1' + ret
                    else:
                        ret = '0' + ret
            else:
                if carry:
                    ret = '0' + ret
                else:
                    ret = '1' + ret
            
            ln -= 1
            
        return '1' + ret if carry else ret
    
        
        