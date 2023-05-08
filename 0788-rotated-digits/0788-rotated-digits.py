class Solution:
    def rotatedDigits(self, n: int) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        self.d = {
            0: 0,
            1: 1,
            2: 5,
            5: 2,
            6: 9,
            9: 6,
            8: 8,
        }
        ret = 0
        
        for i in range(1, n + 1):
            ret += self.solve(i)
            
        return ret
    
    def solve(self, n):
        req = n // 10
        if req not in self.d or n % 10 not in self.d:
            return False
        
        rev = self.d[req] * 10 + self.d[n % 10]
        self.d[n] = rev
            
        return rev != n
    