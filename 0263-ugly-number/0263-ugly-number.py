class Solution:
    def isUgly(self, a: int) -> bool:
        
        # Time: O(sqrt(N))
        # Space: O(N)
        
        if a == 0:
            return False
        
        s = set()
        
        if a < 0:
            a = abs(a)
            s.add(-1)
            
        while a % 2 == 0:
            s.add(2)
            a //= 2
            
        for i in range(3, int(sqrt(a)) + 1, 2):
            
            while a % i == 0:
                s.add(i)
                a //= i
                
        if a > 2:
            s.add(a)
            
        s -= {2, 3, 5}
        
        return False if len(s) else True