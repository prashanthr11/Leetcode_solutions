class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        mp = defaultdict(int)
        mp[0] = 1
        cnt = 0
        sumi = 0
        
        for num in nums:
            sumi = (sumi + num) % k
            cnt += mp[sumi]
            mp[sumi] += 1
            
        return cnt
    