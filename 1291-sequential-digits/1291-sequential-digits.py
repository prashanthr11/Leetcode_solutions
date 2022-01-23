class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        a, b = str(low), str(high)
        ret = []
        
        for i in range(len(a), len(b) + 1):
            j = 1
                
            while True:
                res = self.create_num(j, i, low, high)
                # print(i, j, res)
                if res == -1:
                    break
                    
                if low <= res <= high:
                    ret.append(res)
                    
                j += 1
                
        return ret
    
    
    def create_num(self, start, ln, low, high):
        i = 0
        ret_int = 0
        
        while i < ln:
            if start > 9 or ret_int > high:
                return -1
            
            ret_int = ret_int * 10 + start
            start += 1
            i += 1
            
        return ret_int
    