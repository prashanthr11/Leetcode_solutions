class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        return self.optimise(nums)
    
    def optimise(self, nums):
        d = Counter(nums)
        maxi = 0
        
        for i, a in enumerate(nums):
            if d[a + 1]:
                continue
                
            cnt = 0
            val = a
            
            while d[val]:
                cnt += 1
                val -= 1
                
            maxi = max(maxi, cnt)
            
        return maxi
    