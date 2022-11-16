# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        '''
        Time Complexity: O(log N)
        Space Complexity: O(1)
        '''
        low, high = 1, n
        
        while low <= high:
            mid = (low + high) // 2
            
            api_resp = guess(mid)
            
            if api_resp == -1:
                high = mid
            elif api_resp == 1:
                low = mid + 1
            else:
                return mid
            
    