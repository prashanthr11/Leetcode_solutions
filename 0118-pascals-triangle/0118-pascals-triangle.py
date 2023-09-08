class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        ret = [[1]]
        
        if numRows <= 1:
            return ret
        
        ret.append([1, 1])
        if numRows <= 2:
            return ret
        
        for i in range(3, numRows + 1):
            tmp = [1]
            for j in range(i - 2):
                tmp.append(ret[-1][1 + j] + ret[-1][j])
            tmp.append(1)
            
            ret.append(tmp)
            
        return ret
    