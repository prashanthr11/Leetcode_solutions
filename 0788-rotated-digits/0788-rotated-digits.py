class Solution:
    def rotatedDigits(self, n: int) -> int:
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(1)
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
        n_dup = n
        power = 0
        ret = 0
        
        while n:
            req = n % 10
            if req not in self.d:
                return False
            
            ret += self.d[req] * (10**power)
            power += 1
            n //= 10
            
        return ret != n_dup
    