class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        return self.optimise(nums, k)
    
    
    def optimise(self, nums, k):
        nums = [-i for i in nums]
        heapify(nums)
        return -nsmallest(k, nums)[-1]

    
    def naive(self, nums, k):
        nums.sort()
        return nums[-k]
    