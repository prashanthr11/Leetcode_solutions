class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        return self.optimise(nums, target)
    
    
    def optimise(self, nums, target):
        low, high = 0, len(nums) - 1
        
        while low <= high:
            while low < high and nums[low] == nums[low + 1]:
                low += 1
                
            while low < high and nums[high] == nums[high - 1]:
                high -= 1
                
            mid = low + ((high - low) >> 1)
            
            if nums[mid] == target:
                return True
            
            if nums[low] <= nums[mid]:
                if nums[low] <= target and nums[mid] > target:
                    high = mid - 1
                else:
                    low = mid + 1
            else:
                if nums[mid] < target and target <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        
        return False
    
        
    def naive(self, nums, target):
        return target in nums
    