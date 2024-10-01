class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        return self.naive(nums)
    
    
    def naive(self, nums):
        left_sum = 0
        total_sum = sum(nums)
        
        for i, num in enumerate(nums):
            total_sum -= num
            
            if left_sum == total_sum:
                return i
            
            left_sum += num
            
        return -1
    