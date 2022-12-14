class Solution:
    def rob(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        n = len(nums)
        
        if n <= 2:
            return max(nums)
        
        day_before_yesterday, yesterday = nums[0], max(nums[0], nums[1])
        
        for i in range(2, n):
            temp = yesterday
            yesterday = max(day_before_yesterday + nums[i], yesterday)
            day_before_yesterday = temp
            
        return yesterday
    