class Solution:
    def numSub(self, s: str) -> int:
        return self.solution_2(s)
    
    def solution_1(self, s):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        cnt, ret = 0, 0
        MOD = 10**9 + 7
        
        for i in s:
            if i == "1":
                cnt += 1
            else:
                ret = (ret + cnt * (cnt + 1) // 2) % MOD
                cnt = 0
                
        if cnt:
            ret = (ret + cnt * (cnt + 1) // 2) % MOD
            
        return ret
    
    def solution_2(self, s):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        cnt = ret = 0
        MOD = 10**9 + 7
        
        for i in s:
            if i == "0":
                cnt = 0
                continue
                
            cnt += 1
            ret = (ret + cnt) % MOD
            
        return ret % MOD
    