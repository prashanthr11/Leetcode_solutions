class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(N^3)
        Space Complexity: O(1)
        '''
        cnt = 0
        ln = len(nums)
        
        for i in range(ln):
            for j in range(i + 1, ln):
                if nums[i] != nums[j]:
                    for k in range(j + 1, ln):
                        if nums[i] != nums[k] and nums[j] != nums[k]:
                            cnt += 1
                    
        return cnt
    