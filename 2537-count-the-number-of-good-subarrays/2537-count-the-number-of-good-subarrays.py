class Solution:
    def countGood(self, nums: List[int], K: int) -> int:
        ln = len(nums)
        j = 0
        cnt = k = 0
        d = defaultdict(int)
        
        for i in range(ln):
            while j < ln and k < K:
                k += d[nums[j]]
                d[nums[j]] += 1
                j += 1
                
            if k >= K:
                cnt += ln - (j - 1)

            d[nums[i]] -= 1
            k -= d[nums[i]]
            
        return cnt
