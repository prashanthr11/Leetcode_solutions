class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        result = 0
        i, j, n = 0, 0, len(nums)
        k_ref = k
        
        if k == 0:
            return self.solve(nums)
        
        while j < n:
            while j < n:
                if nums[j] == 0:
                    if k > 0:
                        k -= 1
                    else:
                        break
                    
                j += 1
                        
            result = max(result, j - i)
            
            while i < n and k == 0:
                if nums[i] == 0:
                    k += 1
                
                i += 1
                    
        return result
                    
                    
    def solve(self, nums):
        cnt = 0
        maxi = 0
        
        for num in nums:
            if num == 1:
                cnt += 1
            else:
                cnt = 0
                
            maxi = max(maxi, cnt)
        return maxi
    