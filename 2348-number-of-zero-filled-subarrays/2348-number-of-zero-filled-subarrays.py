class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        
        cnt, ret = 0, 0
        
        for i in nums:
            if i:
                ret += (cnt * (cnt + 1)) // 2
                cnt = 0
            else:
                cnt += 1
        
        if cnt:
            ret += (cnt * (cnt + 1)) // 2
            
        return ret

    