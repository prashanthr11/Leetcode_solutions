class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        '''
        a, b, c
        m, n, o, p
        
        am, an, ao, ap, bm, bn, bo, bp, cm, cn, co, cp
        mn, op, mn, op, mn, op
        mn, op
        
        a, b
        m, n
        
        am, an, bm, bn
        mn, mn
        0
        
        a, b, c
        m, n, o
        
        am, an, ao, bm, bn, bo, cm, cn, co
        mn, mn, ab, mn, c0
        ab, mn, c0
        abcmn0
        
        a, b
        m, n, o
        
        am, an, ao, bm, bn, bo
        mn, mn, ab
        ab
        
        a, b, c, d
        m, n, o, p, q
        
        am, an, ao, ap, aq, bm, bn, bo, bp, bq, cm, cn, co, cp, cq, dm, dn, do, dp, dq
        mn, op, mn, op, ab, mn, op, mn, op, cd
        ab, cd
        '''
        n, m = len(nums1), len(nums2)
        ret = 0
        
        if n % 2:
            if m % 2:
                for i in nums1:
                    ret ^= i
                    
                for i in nums2:
                    ret ^= i
            else:
                for i in nums2:
                    ret ^= i
        else:
            if m % 2:
                for i in nums1:
                    ret ^= i

        return ret
    