class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        '''
        Time Complexity: 2^N
        Space Complexity: 2^N
        '''
        ret = set()
        ln = len(nums)
        
        def solve(i, path):
            
            if len(path) > 1:
                ret.add(tuple(path))
            
            if i >= ln:
                return
            
            for j in range(i, ln):
                if nums[j] >= path[-1]:
                    solve(j + 1, path + [nums[j]])
            
        
        for i in range(ln):
            solve(i + 1, [nums[i]])
            
        return [list(i) for i in ret]