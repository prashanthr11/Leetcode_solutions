class Solution:
    def addBinary(self, a: str, b: str) -> str:
        return self.optimised(a, b)
    
    
    def optimised(self, a, b):
        ln_a, ln_b = len(a) - 1, len(b) - 1
        carry = 0
        pos = max(ln_a, ln_b)
        ret = ["0"] * (pos + 1)
        
        while ln_a >= 0 or ln_b >= 0:
            if ln_a == -1:
                while ln_b >= 0:
                    if b[ln_b] == "1":
                        if carry:
                            ret[pos] = "0"
                        else:
                            ret[pos] = "1"
                    else:
                        if carry:
                            ret[pos] = "1"
                            carry = 0
                        else:
                            ret[pos] = "0"
                    
                    ln_b -= 1
                    pos -= 1
            
            elif ln_b == -1:
                while ln_a >= 0:
                    if a[ln_a] == "1":
                        if carry:
                            ret[pos] = "0"
                        else:
                            ret[pos] = "1"
                    else:
                        if carry:
                            ret[pos] = "1"
                            carry = 0
                        else:
                            ret[pos] = "0"
                    
                    ln_a -= 1
                    pos -= 1
            
            elif a[ln_a] == b[ln_b]:
                if a[ln_a] == "1":
                    if carry:
                        ret[pos] = "1"
                    else:
                        carry = 1
                        ret[pos] = "0"
                else:
                    if carry:
                        ret[pos] = "1"
                        carry = 0
                    else:
                        ret[pos] = "0"
            else:
                if carry:
                    ret[pos] = "0"
                else:
                    ret[pos] = "1"
                    
            ln_a -= 1
            ln_b -= 1
            pos -= 1
            
        if carry:
            ret = "".join(["1"] + ret)
        else:
            ret = "".join(ret)
            
        return ret
    