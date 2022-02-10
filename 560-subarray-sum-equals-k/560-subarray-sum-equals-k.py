class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        
        d[0] = 1
        sumi, cnt = 0, 0
        
        for i in nums:
            sumi += i
            cnt += d[sumi - k]
            d[sumi] += 1
            
        return cnt
    