class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        if k == 0:
            return nums
        
        i, ln = 0, len(nums)
        ret = [-1] * ln
        sumi = 0
        first_idx = 2*k
        denominator = first_idx + 1
        
        while i < ln:
            if i < first_idx:
                sumi += nums[i]
                i += 1
            else:
                sumi += nums[i]
                ret[i - k] = sumi // denominator
                sumi -= nums[i - first_idx]
                i += 1
                
        return ret
    