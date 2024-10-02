class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:

        new_target = sum(nums) - x
        window = deque([])
        ans = float('inf')
        window_sum = 0
        
        for i, a in enumerate(nums):
            
            window_sum += a
            window.append(i)
            
            while window and window_sum > new_target:
                window_sum -= nums[window.popleft()]
                
            if window_sum == new_target:
                no_of_ops = len(nums) - len(window)
                ans = min(ans, no_of_ops)
                
        return ans if ans != float('inf') else -1
        