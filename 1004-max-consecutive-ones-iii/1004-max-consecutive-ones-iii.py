class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zeros_count = 0
        result = 0
        left = 0
        
        for i, num in enumerate(nums):
            if num == 0:
                zeros_count += 1
            
            if zeros_count > k:
                zeros_count -= (nums[left] == 0)
                left += 1
            else:
                result = max(result, i - left + 1)
                
        return result
    