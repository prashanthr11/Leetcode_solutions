from heapq import heapify, nlargest

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        return self.method_1(nums)
    
    def method_1(self, nums):
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(1)
        '''
        nums.sort(reverse=True)
        ln = len(nums)
        
        i, j, k = 0, 1, 2
        while k < ln:
            if nums[i] < nums[j] + nums[k]:
                return nums[i] + nums[j] + nums[k]
            else:
                i = j
                j = k
                k += 1
        
        return 0
    