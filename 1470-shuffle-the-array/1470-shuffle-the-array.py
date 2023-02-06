class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        for i in range(n):
            nums[i] <<= 10
            nums[i] |= nums[i + n]
            
        for i in range(n - 1, -1, -1):
            nums[(2 * i) + 1] = nums[i] & ((1 << 10) - 1)
            nums[2 * i] = nums[i] >> 10
        
        return nums
    