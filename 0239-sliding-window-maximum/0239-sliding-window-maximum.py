class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        if k == 1:
            return nums
        
        ln = len(nums)
        ret = []
        queue = [(-nums[i], i) for i in range(k)]
        heapify(queue)
        i = k
        
        while queue:
            val, idx = queue[0]
            ret.append(-val)
            
            while queue and i - queue[0][1] >= k:
                heappop(queue)
                
            if i < ln:
                heappush(queue, (-nums[i], i))
                i += 1
            else:
                break
                
        return ret
    
            