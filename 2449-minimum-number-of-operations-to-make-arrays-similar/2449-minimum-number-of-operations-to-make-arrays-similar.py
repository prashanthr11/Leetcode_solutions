class Solution:
    def makeSimilar(self, nums: List[int], target: List[int]) -> int:
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(1)
        '''
        nums.sort(key=lambda x:(x&1, x))
        target.sort(key=lambda x:(x&1, x))
        
        sumi = sum(abs(i - j) for i, j in zip(nums, target))
        return sumi >> 2
    