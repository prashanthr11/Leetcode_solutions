class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        lst = deque([])
        sumi = 0
        mini = float('inf')
        
        for i in nums:
            while lst and sumi >= target:
                mini = min(mini, len(lst))
                sumi -= lst.popleft()
                
            sumi += i
            lst.append(i)
            
        while lst and sumi >= target:
            mini = min(mini, len(lst))
            sumi -= lst.popleft()
            
        return mini if mini != float('inf') else 0
    