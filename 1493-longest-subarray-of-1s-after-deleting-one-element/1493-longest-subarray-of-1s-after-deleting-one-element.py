class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        last_ele = (0, -1)
        i, maxi, ln = 0, 0, len(nums)
        
        while i < ln:
            if nums[i] == 0:
                prev_cnt, prev_idx = last_ele
                maxi = max(maxi, i - prev_idx - 1 + prev_cnt)
                last_ele = (i - prev_idx - 1, i)
            i += 1
            
        if last_ele[1] == -1:
            maxi = i - 1
        else:
            prev_cnt, prev_idx = last_ele
            maxi = max(maxi, i - prev_idx - 1 + prev_cnt)
            
        return maxi
    