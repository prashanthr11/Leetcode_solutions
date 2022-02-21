class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return self.optimise(nums)
    
    def optimise(self, nums):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        cnt = 0
        for i in nums:
            if cnt == 0:
                candidate = i
                
            cnt += 1 if i == candidate else -1
            
        return candidate
    
    def naive(self, nums):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        '''
        ln = len(nums)
        mid = ln // 2
        for i in range(ln):
            cnt = 0
            for j in range(i + 1, ln):
                if nums[i] == nums[j]:
                    cnt += 1
                    
            if cnt >= mid:
                ret = nums[i]
                
        return ret
    
    def method_1(self, nums):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        d = Counter(nums)
        ln = len(nums)
        mid = ln // 2
        
        for k, v in d.items():
            if v >= mid:
                return k
            