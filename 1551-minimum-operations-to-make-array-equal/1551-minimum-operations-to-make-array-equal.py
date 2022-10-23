class Solution:
    def minOperations(self, n: int) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        mid = (n // 2) * 2 + 1 if n % 2 else (n // 2) * 2
        sumi = 0
        
        for i in range(n):
            sumi += abs(2 * i + 1 - mid)
        
        return sumi >> 1
    