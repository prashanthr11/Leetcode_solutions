class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return self.solve(nums, target)
        
    def inbuilt(self, nums, target):
        return bisect.bisect_left(nums, target)
    
    
    def solve(self, nums, target):
        low, high = 0, len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
                
        return low
    