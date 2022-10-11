class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        return self.even_optimise(nums)
    
    def even_optimise(self, nums):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)        
        '''
        left = mid = float('inf')
        
        for i in nums:
            if i <= left:
                left = i
            elif i <= mid:
                mid = i
            else:
                return True
            
        return False
    
    def naive(self, nums):
        '''
        Time Complexity: O(N^3)
        Space Complexity: O(1)
        '''
        ln = len(nums)
        
        for i in range(ln):
            for j in range(i + 1, ln):
                if nums[i] < nums[j]:
                    for k in range(j + 1, ln):
                        if nums[j] < nums[k]:
                            return True

        return False
    
    def test(self, nums, idx=0):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        ln = len(nums)
        minis = [0] * ln
        maxis = [0] * ln
        
        for i in range(ln):
            if not i:
                minis[i] = nums[i]
                maxis[ln - i - 1] = nums[ln - i - 1]
            else:
                minis[i] = min(nums[i], minis[i - 1])
                maxis[ln - i - 1] = max(nums[ln - i - 1], maxis[ln - i])
                        
        for i in range(ln):
            if minis[i] < nums[i] < maxis[i]:
                return True
            
        return False
    