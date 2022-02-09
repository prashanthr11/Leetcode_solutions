class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        return self.solve(nums, k)
    
    def solve(self, nums, k):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        d = Counter(nums)
        keys = set(d)
        cnt = 0
        
        for key in keys:
            if k > 0 and k + key in d:
                cnt += 1
                
            if k == 0 and d[key] > 1:
                cnt += 1
                
        return cnt
    
    def optimise(self, nums, k):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        vis = set()
        ret = set()
        
        for i in nums:
            if i + k in vis:
                if i < i + k:
                    ret.add((i, i + k))
                else:
                    ret.add((i + k, i))
            
            if i - k in vis:
                if i < i - k:
                    ret.add((i, i - k))
                else:
                    ret.add((i - k, i))
            
            vis.add(i)
            
        print(ret)
        return len(ret)
    
    def naive(self, nums, k):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        '''
        pairs = set()
        ln = len(nums)
        
        for i in range(ln):
            for j in range(i + 1, ln):
                if abs(nums[i] - nums[j]) == k:
                    if nums[i] > nums[j]:
                        pairs.add((nums[j], nums[i]))
                    else:
                        pairs.add((nums[i], nums[j]))
        
        print(pairs)
        return len(pairs)
    