class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        cnt = 0
        
        while c or a or b:
            a_last_bit = a & 1
            b_last_bit = b & 1
            c_last_bit = c & 1
            
            if (a_last_bit | b_last_bit) != c_last_bit:
                if c_last_bit:
                    cnt += 1
                else:
                    if a_last_bit:
                        cnt += 1
                        
                    if b_last_bit:
                        cnt += 1
                        
            a >>= 1
            b >>= 1
            c >>= 1
        
        return cnt
    