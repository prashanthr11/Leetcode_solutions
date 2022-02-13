class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        '''
        Time Complexity: O(2^N)
        Space Time Complexity: O(2^N)
        '''
        def solve(i, n, nums, vis):
            ret.append([i for i in vis])

            for j in range(i, n):
                solve(j + 1, n, nums, vis + [nums[j]])

        ret = []
        solve(0, len(nums), nums, [])
        
        return ret
        