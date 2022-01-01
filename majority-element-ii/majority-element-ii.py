class Solution:
    def approach_2(self, nums):
        '''
        Time Complexity: O(N) -> where N is the length of the given array.
        Space Complexity: O(N)
        '''
        ln = len(nums)
        ret = []
        d = Counter(nums)
        
        for k, v in d.items():
            if v > ln // 3:
                ret.append(k)
                
        return ret
    
    def approach_1(self, nums):
        '''
        Time Complexity: O(N LogN) -> where N is the length of the given array.
        Space Complexity: O(1)
        '''    
        ret = []
        ln = len(nums)
        nums.sort()
        i, j = 0, 0
        while i < ln:
            j = i + 1
            cnt = 1
            while j < ln and nums[i] == nums[j]:
                cnt += 1
                j += 1
            
            if cnt > ln // 3:
                ret.append(nums[i])
            i = j
            
        return ret
    
    
    def solve(self, nums, first_mem=None, second_mem=None, third_mem=None):
        
        candidate = None
        count = 0
        for i in nums:
            if i == first_mem or second_mem == i or i == third_mem:
                continue
                
            if count == 0:
                candidate = i
                
            count += 1 if candidate == i else -1
        
        return candidate
        
    def majorityElement(self, nums: List[int]) -> List[int]:
        return self.approach_2(nums)
    
        '''
        ret = []
        ln = len(nums)
        min_freq = ln // 3
        
        first_mem = self.solve(nums)
        
        if nums.count(first_mem) > min_freq:
            ret.append(first_mem)
            
        second_mem = self.solve(nums, first_mem=first_mem)
        if nums.count(second_mem) > min_freq:
            ret.append(second_mem)
                       
        third_mem = self.solve(nums, first_mem=first_mem, second_mem=second_mem)
        if nums.count(third_mem) > min_freq:
            ret.append(third_mem)
            
        return ret
        '''