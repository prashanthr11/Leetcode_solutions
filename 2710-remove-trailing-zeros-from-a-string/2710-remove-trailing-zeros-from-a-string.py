class Solution:
    def removeTrailingZeros(self, num: str) -> str:
        return num.rstrip("0")
        
    def naive(self, num):
        i, n = 0, len(num)
        
        while i < n and num[i] == '0':
            i += 1
            
        while i <= n and num[n - 1] == '0':
            n -= 1
            
        return num[i:n]