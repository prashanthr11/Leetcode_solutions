class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        ones_count = 0
        result = 0
        left = 0
        
        for i, num in enumerate(nums):
            if num == 1:
                ones_count += 1
                
            no_of_zeros = i - left + 1 - ones_count
            
            if no_of_zeros <= k:
                result = max(result, i - left + 1)
            else:
                ones_count -= (nums[left] == 1)
                left += 1
                
        return result
