class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        return self.optimised(nums1, nums2, nums3, nums4)
    
    def optimised(self, nums1, nums2, nums3, nums4):
        '''
        Time Complexity: O(N^2)
        Space Complexity: O(N^2)
        '''
        d = defaultdict(int)
        cnt = 0
        
        for i in nums1:
            for j in nums2:
                d[i + j] += 1
                
        for i in nums3:
            for j in nums4:
                if -(i + j) in d:
                    cnt += d[-(i + j)]
                    
        return cnt
    
    
    def naive(self, nums1, nums2, nums3, nums4):
        '''
        Time Complexity: O(N^4)
        Space Complexity: O(1)
        '''
        cnt = 0
        
        for i in nums1:
            for j in nums2:
                for k in nums3:
                    for a in nums4:
                        if i + j + k + a == 0:
                            cnt += 1
                            
        return cnt
    