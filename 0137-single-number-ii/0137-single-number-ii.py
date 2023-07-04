class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return self.optimise(nums)
    
    def optimise(self, nums):
        ln = len(nums)
        nums.sort()
        
        for i in range(0, ln, 3):
            if i + 1 < ln and nums[i] != nums[i + 1]:
                return nums[i]
        
        return nums[i]
    
    def naive(self, nums):
        d = Counter(nums)
        
        for k, v in d.items():
            if v == 1:
                return k
            