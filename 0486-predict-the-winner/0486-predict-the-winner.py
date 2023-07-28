class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        def solve(low, high):
            
            if low == high:
                return nums[low]
            
            return max(nums[low] - solve(low + 1, high), nums[high] - solve(low, high - 1))
        
        return solve(0, len(nums) - 1) >= 0
    