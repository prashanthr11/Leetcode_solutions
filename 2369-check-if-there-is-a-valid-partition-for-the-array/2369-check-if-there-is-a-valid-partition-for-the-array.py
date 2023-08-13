class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        ln = len(nums)
        
        @cache
        def solve(idx):
            if idx <= 0:
                return idx == -1
            
            if nums[idx] == nums[idx - 1]:
                if idx - 2 >= 0 and nums[idx - 2] == nums[idx]:
                    return solve(idx - 3) or solve(idx - 2)
                else:
                    return solve(idx - 2)
            else:
                if idx - 2 >= 0 and nums[idx] - nums[idx - 1] == nums[idx - 1] - nums[idx - 2] == 1:
                    return solve(idx - 3)

                return False
            
        return solve(ln - 1)
    