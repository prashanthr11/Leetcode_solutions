class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        return self.optimise(nums)
    
    def optimise(self, nums):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        d = {}
        d[0] = -1
        maxi, cnt = 0, 0
        
        for i in range(len(nums)):
            cnt += -1 if nums[i] == 0 else 1
            
            if cnt in d:
                maxi = max(maxi, i - d[cnt])
            else:
                d[cnt] = i
                
        return maxi
    
    def naive(self, nums):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        '''
        maxi = 0
        ln = len(nums)
        
        for i in range(ln):
            counter = 0
            for j in range(i, ln):
                counter += 1 if nums[j] else -1
                
                if counter == 0:
                    maxi = max(maxi, j - i + 1)
                    
        return maxi
    