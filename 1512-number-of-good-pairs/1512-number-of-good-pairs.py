class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        return self.optimise(nums)
    
    
    def optimise(self, nums):
        '''
        TC: O(N)
        SC: O(N)
        '''
        d = defaultdict(int)
        cnt = 0
        
        for i, a in enumerate(nums):
            d[a] += 1
            
        for k, v in d.items():
            cnt += (v * (v - 1) // 2)
        
        return cnt
    
    
    def naive(self, nums):
        '''
        TC: O(N^2)
        SC: O(1)
        '''
        ln = len(nums)
        cnt = 0
        
        for i in range(ln):
            for j in range(i + 1, ln):
                cnt += (nums[i] == nums[j])
                
        return cnt
    