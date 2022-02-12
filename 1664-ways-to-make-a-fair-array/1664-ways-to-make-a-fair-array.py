class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        return self.optimise(nums)
    
    def naive(self, nums):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        '''
        cnt = 0
        ln = len(nums)
        
        for i in range(ln):
            sumi = 0
            sign = '+'
            for j in range(ln):
                if i == j:
                    continue
                    
                if sign == '-':
                    sumi -= nums[j]
                    sign = '+'
                else:
                    sumi += nums[j]
                    sign = '-'
                    
            print(sumi)
            if sumi == 0:
                cnt += 1
            
        return cnt
    
    def optimise(self, nums):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        ln = len(nums)
        cnt = 0
        even_prefs = [0] * (ln + 1)
        odd_prefs = [0] * (ln + 1)
                
        for i in range(ln):
            if i % 2:
                odd_prefs[i + 1] = odd_prefs[i] + nums[i]
                even_prefs[i + 1] = even_prefs[i]
            else:
                even_prefs[i + 1] = even_prefs[i] + nums[i]
                odd_prefs[i + 1] = odd_prefs[i]
                
        for i in range(ln):
            sumi = even_prefs[i] - odd_prefs[i]
            sumi += odd_prefs[-1] - odd_prefs[i + 1]
            sumi -= even_prefs[-1] - even_prefs[i + 1]
            
            if sumi == 0:
                cnt += 1
                
        return cnt
    