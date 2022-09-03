class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.ret = []
        digits = [i for i in range(1, 10)]
        
        for i in digits:
            self.solve(i, k, n - 1, str(i))
                
        return list(set(self.ret))
    
    def solve(self, i, k, n, path):
        if n <= 0:
            self.ret.append(int(path))
            return 
        
        if int(path[-1]) + k <= 9:
            self.solve(i, k, n - 1, path + str(int(path[-1]) + k))
        
        if int(path[-1]) - k >= 0:
            self.solve(i, k, n - 1, path + str(int(path[-1]) - k))
        '''
        n = 3
        k = 2
        
        1 3 5
        1 3 1
        2 0 2
        2 4 6
        2 4 2
        3 1 3
        3 5 7
        3 5 3
        4 2 4
        4 2 0
        4 6 8
        4 6 4
        5 3 5
        5 3 1
        5 7 9
        5 7 5
        6 4 6
        6 4 2
        6 8 6
        7 5 7
        7 5 3
        7 9 7
        8 6 8
        8 6 4
        9 7 9
        9 7 5
        '''