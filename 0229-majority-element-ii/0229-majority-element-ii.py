class Solution:
    def approach_2(self, nums):
        '''
        Time Complexity: O(N) -> where N is the length of the given array.
        Space Complexity: O(N)
        '''
        ln = len(nums)
        ret = []
        d = Counter(nums)
        
        for k, v in d.items():
            if v > ln // 3:
                ret.append(k)
                
        return ret
    
    def approach_1(self, nums):
        '''
        Time Complexity: O(N LogN) -> where N is the length of the given array.
        Space Complexity: O(1)
        '''    
        ret = []
        ln = len(nums)
        nums.sort()
        i, j = 0, 0
        while i < ln:
            j = i + 1
            cnt = 1
            while j < ln and nums[i] == nums[j]:
                cnt += 1
                j += 1
            
            if cnt > ln // 3:
                ret.append(nums[i])
            i = j
            
        return ret
    
            
    def majorityElement(self, nums: List[int]) -> List[int]:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        max1, max2, cnt1, cnt2 = None, None, 0, 0
        
        for i in nums:
            if i == max1:
                cnt1 += 1
            elif i == max2:
                cnt2 += 1
            elif cnt1 == 0:
                max1 = i
                cnt1 = 1
            elif cnt2 == 0:
                max2 = i
                cnt2 = 1
            else:
                cnt1 -= 1
                cnt2 -= 1
                
        return [i for i in [max1, max2] if i is not None and nums.count(i) > len(nums) // 3]