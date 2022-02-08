class Solution:
    def addDigits(self, num: int) -> int:
        '''
        Time Complexity: O(Log N)
        Space Complexity: O(1)
        '''
        while num // 10:
            new_num = 0
            while num:
                new_num += (num % 10)
                num //= 10
                
            num = new_num
                
        return num
    