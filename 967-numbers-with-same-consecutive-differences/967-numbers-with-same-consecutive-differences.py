class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.ret = []
        digits = [i for i in range(1, 10)]
        
        for i in digits:
            self.solve(i, k, n - 1, i)
                
        return list(set(self.ret))
    
    def solve(self, i, k, n, path):
        if n <= 0:
            self.ret.append(path)
            return 
        
        if (path % 10) + k <= 9:
            self.solve(i, k, n - 1, (path * 10) + (path % 10) + k)
            
        if (path % 10) - k >= 0:
            self.solve(i, k, n - 1, (path * 10) + (path % 10) - k)
