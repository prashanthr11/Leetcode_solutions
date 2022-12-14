class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        
        if n <= 2:
            return max(nums)
        
        dp = [float('inf')] * n
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        
        for i in range(2, n):
            dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            
        return dp[-1]
    