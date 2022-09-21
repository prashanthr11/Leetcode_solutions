class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        return self.solve(nums1, nums2)
    
    def solve(self, nums1, nums2):
        '''
        Time Complexity: O(M*N)
        Space Complexity: O(M*N)
        '''
        n, m = len(nums1), len(nums2)
        dp = [[0]*(m + 1) for i in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                if nums1[i] == nums2[j]:
                    dp[i][j] = 1 + dp[i + 1][j + 1]

        maxi = 0
        for xx in dp:
            maxi = max(maxi, max(xx))
            
        return maxi
    

        
        