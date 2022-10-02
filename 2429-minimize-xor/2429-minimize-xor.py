class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        return self.optimise(num1, num2)
        
        
    def optimise(self, num1, num2):
        a, b = num1.bit_count(), num2.bit_count()
        
        if a == b:
            return num1
        
        ret = 0
        for i in range(31, -1, -1):
            if b > 0 and num1 & (1 << i):
                ret |= (1 << i)
                b -= 1
                
        for i in range(32):
            if b == 0:
                break
                
            if num1 & (1 << i) == 0:
                ret |= (1 << i)
                b -= 1
                
        return ret
        
    
    def naive(self, num1, nums2):
        one_bin = bin(num1)[2:]
        two_bin = bin(num2)[2:]
        
        one_cnt = one_bin.count('1')
        two_cnt = two_bin.count('1')
        
        if one_cnt == two_cnt:
            return num1
        elif one_cnt < two_cnt:
            ret = 0
            one_bin = one_bin[::-1]
            zeros = [i for i in range(len(one_bin)) if one_bin[i] != "1"]
            ones = [i for i in range(len(one_bin)) if one_bin[i] == "1"][::-1]
            ones_pos = len(ones) - 1
            zeros_pos = 0
            
            while two_cnt:
                if ones_pos < 0:
                    if zeros_pos < len(zeros):
                        ret |= (1 << zeros[zeros_pos])
                        zeros_pos += 1
                    else:
                        ret <<= 1
                        ret |= 1
                else:
                    if ones_pos == len(ones) - 1:
                        ret = 1 << ones[ones_pos]
                    else:
                        tmp = 1 << ones[ones_pos]
                        ret |= tmp
                    ones_pos -= 1
                two_cnt -= 1
        else:
            ret = 0
            cpy = one_bin[::-1]
            ones = [i for i in range(len(one_bin)) if cpy[i] == "1"]
            pos = len(ones) - 1
            while two_cnt:
                if pos == len(ones) - 1:
                    ret = 1 << ones[pos]
                else:
                    tmp = 1 << ones[pos]
                    ret |= tmp
                two_cnt -= 1
                pos -= 1
                
        return ret
            
