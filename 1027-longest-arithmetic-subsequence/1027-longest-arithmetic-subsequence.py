class Solution:
    def longestArithSeqLength(self, nums: List[int]) -> int:
        d = {}
        n = len(nums)
        
        for i in range(n):
            for j in range(i):
                d[(i, nums[i] - nums[j])] = d.get((j, nums[i] - nums[j]), 1) + 1
                
        return max(d.values())
    