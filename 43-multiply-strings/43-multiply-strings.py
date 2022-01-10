class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        '''
        return str(int(num1) * int(num2))
        '''
        a = self.convert(num1)
        # print(a)
        n = len(num2)
        cnt = 1
        ans = 0
        
        for i in range(n - 1, -1, -1):
            res = self.multiply_(ord(num2[i]) - ord('0'), a)
            res = res * cnt
            cnt *= 10
            ans += res
            
        return str(ans)
    
    
    def multiply_(self, m, n):
        return n * m
    
    
    def convert(self, n):
        ret = 0
        for i in n:
            ret = ret * 10 + (ord(i) - ord('0'))
            
        return ret
        