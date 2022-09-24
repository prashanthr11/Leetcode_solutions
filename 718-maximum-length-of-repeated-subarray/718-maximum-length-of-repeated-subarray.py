class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        return self.optimise(nums1, nums2)
        
    def dp(self, nums1, nums2):
        '''
        Time Complexity: O(M*N)
        Space Complexity: O(M*N)
        '''
        n, m = len(nums1), len(nums2)
        
        dp = [[0]*(n + 1) for i in range(m + 1)]
        
        for i in range(n):
            for j in range(m):
                if nums1[i] == nums2[j]:
                    dp[i + 1][j + 1] = 1 + dp[i][j]
                    
        return max([max(i) for i in dp])
    
    def optimise(self, nums1, nums2):
        '''
        Time Complexity: O(M*N)
        Space Complexity: O(1)
        '''
        B, A = sorted([nums2, nums1], key=len)
        n, m = len(B), len(A)
        maxi = 0
        
        for i in range(-n + 1, n + m - 1):
            cnt = 0
            for j in range(n):
                top_idx = i + j
                if top_idx < 0:
                    continue
                    
                if top_idx >= m:
                    break
                    
                if B[j] == A[top_idx]:
                    cnt += 1
                    maxi = max(maxi, cnt)
                else:
                    cnt = 0
                    
        return maxi
    