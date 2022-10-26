class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        return self.optimise(nums, k)
    
    def naive(self, nums, k):
        ln = len(nums)
        pref = [0]
        
        for i in range(ln):
            pref.append(pref[-1] + nums[i])
            
        for i in range(ln):
            for j in range(i + 1, ln):
                sumi = pref[j + 1] - pref[i]
                
                if sumi % k == 0:
                    return True
                
        return False
    
    
    def optimise(self, nums, k):
        d = {
            0: -1
        }
        sumi = 0
        
        for i, a in enumerate(nums):
            sumi += (a % k)
            
            if sumi % k not in d:
                d[sumi % k] = i
            else:
                if i - d[sumi % k] > 1:
                    return True
            
        return False

    