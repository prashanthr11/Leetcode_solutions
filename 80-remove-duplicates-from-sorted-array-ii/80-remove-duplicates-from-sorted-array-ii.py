class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        return self.method_2(nums)
    
    def method_2(self, nums):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        i, ln = 0, len(nums)
        pos = 0
        
        while i < ln:
            nums[pos] = nums[i]
            pos += 1
            i += 1
            
            if i < ln and nums[i] == nums[i - 1]:
                nums[pos] = nums[i]
                pos += 1
                i += 1

            while i < ln and nums[i] == nums[i - 1]:
                i += 1
                
        return pos
    
    def method_1(self, nums):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        d = Counter(nums)
        pos = 0
        
        for k, v in d.items():
            if v > 1:
                nums[pos] = k
                pos += 1
                nums[pos] = k
            else:
                nums[pos] = k
                
            pos += 1
            
        return pos
    