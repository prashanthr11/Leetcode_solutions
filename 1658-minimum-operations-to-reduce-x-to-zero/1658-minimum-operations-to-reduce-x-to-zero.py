class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        new_target = sum(nums) - x
        left = 0
        ans = float('inf')
        window_sum = 0
        
        for i, a in enumerate(nums):
            
            window_sum += a
            
            while left <= i and window_sum > new_target:
                window_sum -= nums[left]
                left += 1
                
            if window_sum == new_target:
                no_of_ops = len(nums) - (i - left + 1)
                ans = min(ans, no_of_ops)
                
        return ans if ans != float('inf') else -1
        