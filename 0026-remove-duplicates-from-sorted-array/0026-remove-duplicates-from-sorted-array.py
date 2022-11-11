class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        i, ln = 1, len(nums)
        
        while i < ln:
            if nums[i] == nums[i - 1]:
                nums[i - 1] = -101
                
            i += 1
            
        pos = i = 0
        while i < ln:
            while i < ln and nums[i] == -101:
                i += 1
            
            nums[pos] = nums[i]
            pos += 1
            i += 1
            
        return pos
    