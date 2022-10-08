from bisect import *

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        return self.optimise(nums, target)
    
    def optimise(self, nums, target):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(1)
        '''
        ln = len(nums)
        mini = float('inf')
        nums.sort()
        
        for i in range(ln - 2):
            j = i + 1
            k = ln - 1
            
            while j < k:
                sumi = nums[i] + nums[j] + nums[k]
                
                if mini > abs(target - sumi):
                    mini = abs(target - sumi)
                    ret = sumi
                    
                if mini == 0:
                    return target
                elif sumi > target:
                    k -= 1
                else:
                    j += 1
                    
        return ret
    
    def solve(self, nums, target):
        '''
        Time Complexity: O(N^2 logN)
        Space Complexity: O(1)
        '''
        nums.sort()
        ln = len(nums)
        mini = float('inf')
        
        for i in range(ln):
            for j in range(i + 1, ln):
                idx = bisect(nums, target - nums[i] - nums[j])
                
                if idx:
                    if idx < ln:
                        sumi = nums[i] + nums[j] + nums[idx]
                        if mini > abs(target - sumi):
                            mini = abs(target - sumi)
                            ret = sumi
                        
                    if idx - 1 != i and idx - 1 != j:
                        sumi = nums[i] + nums[j] + nums[idx - 1]
                        if mini > abs(target - sumi):
                            mini = abs(target - sumi)
                            ret = sumi
        
        return ret
                        
        
                
    def naive(self, nums, target):
        '''
        Time Complexity: O(N^3)
        Space Complexity: O(1)
        '''
        ln = len(nums)
        mini = float('inf')
        
        for i in range(ln):
            for j in range(i + 1, ln):
                for k in range(j + 1, ln):
                    sumi = nums[i] + nums[j] + nums[k]
                    if abs(target - sumi ) < mini:
                        mini = abs(target - sumi)
                        ret = sumi
                        
        return ret