class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        d = dict()
        cnt = 0
        n = len(nums)
        ret = 0
        
        for i in range(n):
            cnt += 1 if nums[i] else -1
            
            if cnt == 0:
                ret = max(ret, i + 1)
                
            if cnt in d:
                ret = max(ret, i - d[cnt])
            else:
                d[cnt] = i
                
        return ret
        
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        
        ret = 0
        n = len(nums)
        
        for i in range(n):
            cnt = 0
            for j in range(i, n):
                cnt += 1 if nums[j] == nums[i] else -1
                if cnt == 0:
                    ret = max(ret, j - i + 1)
                    
        return ret
        '''