class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        n = len(nums)
        mini = float('inf')
        idx = -1
        total_sum = sum(nums)
        sumi = 0
            
        for i in range(n):
            sumi += nums[i]
            last = total_sum - sumi
            
            first_avg = int(sumi / (i + 1))
            last_avg = int(last / (n - i - 1)) if last else 0
            
            ans = abs(first_avg - last_avg)
            if ans < mini:
                mini = ans
                idx = i
                
        return idx
    