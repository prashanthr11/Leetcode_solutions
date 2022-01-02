class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        ret = [0] * 60
        
        for i in time:
            ret[i % 60] += 1
            
        cnt = 0
        if ret[0]:
            cnt += (ret[0] * (ret[0] - 1)) // 2
            
        if ret[30]:
            cnt += (ret[30] * (ret[30] - 1)) // 2
            
        for i in range(1, 30):
            cnt += (ret[i] * ret[60 - i])
                
        return cnt