class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        '''
        Time Complexity: O(Log(Bound, x) * Log(Bound, y))
        Space Complexity: O(Log(Bound, x) * Log(Bound, y))
        '''
        st = set()
        
        if x == 1 or y == 1:
            if x == 1 and y == 1:
                return [2] if bound >= 2 else []
            
            if x != 1:
                x, y = y, x
                
            return list(self.solve(x, 0, y, bound))
        
        x_pow = 0
        while x**x_pow <= bound:
            tmp_st = self.solve(x, x_pow, y, bound)
            st = st.union(tmp_st)
            x_pow += 1
            
        return list(st)
    
    def solve(self, x, x_pow, y, bound):
        st = set()
        y_pow = 0
        
        while True:
            res = x ** x_pow + y ** y_pow
            if res > bound:
                break

            st.add(res)
            y_pow += 1

        return st
