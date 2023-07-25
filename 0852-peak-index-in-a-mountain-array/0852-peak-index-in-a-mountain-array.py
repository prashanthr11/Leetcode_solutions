class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        return self.optimise(arr)
        
        
    def optimise(self, nums):
        low, high = 0, len(nums) - 1
        
        while low < high:
            mid = low + (high - low) // 2

            if nums[mid - 1] < nums[mid] > nums[mid + 1]:
                return mid
            
            if nums[mid] < nums[mid + 1]:
                low = mid + 1
            else:            
                high = mid
                
                    
    def naive(self, arr):
        ln = len(arr)
        
        for i in range(1, ln):
            if arr[i - 1] > arr[i]:
                return i - 1
            
             