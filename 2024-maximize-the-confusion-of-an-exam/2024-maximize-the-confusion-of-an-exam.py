class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        max_size = 0
        count = collections.Counter()
        
        for right in range(len(answerKey)):
            count[answerKey[right]] += 1
            minor = min(count['T'], count['F'])
            
            if minor <= k:
                max_size += 1
            else:
                count[answerKey[right - max_size]] -= 1

        return max_size
    
    
    def naive(self, nums, k):
        ln = len(nums)
        i = 0
        maxi = 0
        
        while i < ln:
            j = i + 1
            temp_k = k
            while j < ln:
                if nums[i] == nums[j]:
                    j += 1
                    continue
                    
                if temp_k <= 0:
                    break
                    
                if nums[i] != nums[j]:
                    temp_k -= 1
                    j += 1
                    
            maxi = max(maxi, j - i)
            cur = nums[i]
            
            while i < ln and cur == nums[i]:
                i += 1
                
        return maxi
            