class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        i, ln = 0, len(nums)
        ret = []
        
        if ln < 1:
            return nums
        
        if ln == 1:
            return [str(i) for i in nums]
        
        start = nums[i]
        end = nums[i]
        
        while i + 1 < ln:
            if nums[i + 1] - nums[i] != 1:
                if end > start:
                    ret.append(f"{start}->{end}")
                else:
                    ret.append(str(start))
                start = nums[i + 1]
            else:
                end = nums[i + 1]
                
            i += 1
            
        if end > start:
            ret.append(f"{start}->{end}")
        else:
            ret.append(f"{start}")
        
        return ret
    