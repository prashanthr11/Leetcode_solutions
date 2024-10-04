class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = m - 1, n - 1
        pos = i + j + 1
        
        while i >= 0 or j >= 0:
            if i >= 0 and j >= 0:
                if nums1[i] <= nums2[j]:
                    nums1[pos] = nums2[j]
                    j -= 1
                else:
                    nums1[pos] = nums1[i]
                    i -= 1
            else:
                if i == -1:
                    nums1[pos] = nums2[j]
                    j -= 1
                else:
                    nums1[pos] = nums1[i]
                    i -= 1
                    
            pos -= 1
            
        