from heapq import *

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return self.exp(nums, k)
    
    def exp(self, nums, k):
        di = Counter(nums)
        l = [(-j, i) for i, j in di.items()]
        heapify(l)
        return [i[1] for i in nsmallest(k, l)]
    
    def naive(self, nums, k):
        di = Counter(nums)
        l = sorted(di, key=lambda x:-di[x])
        return l[:k]