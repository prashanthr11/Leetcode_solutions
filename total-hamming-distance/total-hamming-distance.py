class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        ret = 0
        ln = len(nums)
        
        for i in range(32):
            set_bits = 0
            for n in nums:
                set_bits += ((n >> i) & 1 == 1)
                
            ret += set_bits * (ln - set_bits)
        
        return ret
    