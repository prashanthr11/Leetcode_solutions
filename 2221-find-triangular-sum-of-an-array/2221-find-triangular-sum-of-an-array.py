class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        '''
        ln = len(nums)
        
        while ln != 1:
            i = 0
            
            while i + 1 < ln:
                nums[i] = (nums[i] + nums[i + 1]) % 10
                i += 1
            
            ln -= 1
            
        return nums[0]
    