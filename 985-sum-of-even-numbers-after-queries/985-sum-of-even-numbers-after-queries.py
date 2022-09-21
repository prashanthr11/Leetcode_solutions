class Solution:
    def sumEvenAfterQueries(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        sumi = sum([i for i in nums if i % 2 == 0])
        ln = len(queries)
        ret = [0] * ln
        
        for i in range(ln):
            val, index = queries[i]
            value_flag = abs(val) % 2 == 0
            
            if abs(nums[index]) % 2:
                if value_flag:
                    nums[index] += val
                else:
                    nums[index] += val
                    sumi += nums[index]
            else:
                if value_flag:
                    nums[index] += val
                    sumi += val
                else:
                    sumi -= nums[index]
                    nums[index] += val
                
            ret[i] = sumi
                
        return ret