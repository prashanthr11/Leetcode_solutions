class Solution:
    def maximumSwap(self, num: int) -> int:
        
        maxi = num
        
        nums = list(map(str, str(num)))
        
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                new_num = int(''.join(nums))
                maxi = max(maxi, new_num)
                nums[i], nums[j] = nums[j], nums[i]
                
                
        return maxi
    