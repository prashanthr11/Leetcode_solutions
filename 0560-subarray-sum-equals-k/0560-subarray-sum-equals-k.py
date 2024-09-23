class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        cnt = 0
        sumi = 0
        
        for i in nums:
            sumi += i
            cnt += mp[sumi - k]
            mp[sumi] += 1
            
        return cnt
    