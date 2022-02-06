class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        return self.optimise(nums, k)
        
    def optimise(self, nums, k):
        d = Counter(nums)
        keys = sorted(d.keys())
        
        i, ln = 0, len(keys)
        while i < ln:
            while d[keys[i]]:
                for j in range(k):
                    if d[keys[i] + j] <= 0:
                        return False
                    
                    d[keys[i] + j] -= 1
                    
            i += 1
            
        return True
        
    def naive(self, nums, k):
        while nums:
            mini = min(nums)
            
            for i in range(k):
                if mini + i in nums:
                    nums.remove(mini + i)
                else:
                    return False
                
        return True
    