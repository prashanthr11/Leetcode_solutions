class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)
        ln = n + m
        mid, flag = divmod(ln, 2)
        i, j = 0, 0
        cnt = 0
        prev = 0
        
        while i < n or j < m:
                
            if i == n:
                while j < m and cnt < mid:
                    prev = nums2[j]
                    cnt += 1
                    j += 1
            
            if j == m:
                while i < n and cnt < mid:
                    prev = nums1[i]
                    cnt += 1
                    i += 1
            
            if cnt == mid:
                if flag:
                    if i == n:
                        return nums2[j]
                    elif j == m:
                        return nums1[i]
                    else:
                        return min(nums1[i], nums2[j])
                else:
                    if i == n:
                        return (prev + nums2[j]) / 2
                    elif j == m:
                        return (prev + nums1[i]) / 2
                    else:
                        return (prev + min(nums1[i], nums2[j])) / 2
            
            if nums1[i] <= nums2[j]:
                prev = nums1[i]
                i += 1
                cnt += 1
            else:
                prev = nums2[j]
                j += 1
                cnt += 1
                