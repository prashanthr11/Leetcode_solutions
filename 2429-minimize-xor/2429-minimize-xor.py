class Solution:
    def minimizeXor(self, num1: int, num2: int) -> int:
        # return self.naive(num1, num2)
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
            
        
    def naive(self, num1, num2):
        bits = self.get_set_bits(num2)
        ones_bits = self.get_set_bits(num1)

        if ones_bits < bits:
            ret = 0
            binn = bin(num1)[2:][::-1]
            zeros = [i for i in range(len(binn)) if binn[i] != "1"]
            ones = [i for i in range(len(binn)) if binn[i] == "1"][::-1]
            ones_pos = len(ones) - 1
            zeros_pos = 0
            
            while bits:
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
                bits -= 1
                
        elif ones_bits == bits:
            ret = num1
        else:
            ret = 0
            binn = bin(num1)[2:][::-1]
            lst = [i for i in range(len(binn)) if binn[i] == "1"]
            pos = len(lst) - 1
            while bits:
                if pos == len(lst) - 1:
                    ret = 1 << lst[pos]
                else:
                    tmp = 1 << lst[pos]
                    ret |= tmp
                bits -= 1
                pos -= 1
            
        return ret
    
    def get_set_bits(self, x):
        cnt = 0
        
        while x:
            cnt = cnt + 1 if x & 1 else cnt
            x >>= 1
            
        return cnt
