class Solution:
    def climbStairs(self, n: int) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        second_last, last = 0, 1
        
        for i in range(n):
            temp = last
            last += second_last
            second_last = temp

        return last