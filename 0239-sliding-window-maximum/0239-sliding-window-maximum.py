class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:        
        ln = len(nums)
        ret = []
        queue = deque([])
        
        for i in range(k):
            while queue and nums[queue[-1]] <= nums[i]:
                queue.pop()
                
            queue.append(i)

        i = k
        while i <= ln:
            ret.append(nums[queue[0]])
            
            if i == ln:
                break
            
            while queue and i - queue[0] >= k:
                queue.popleft()
                
            while queue and nums[i] >= nums[queue[-1]]:
                queue.pop()
                
            queue.append(i)
            i += 1
            
        return ret
    