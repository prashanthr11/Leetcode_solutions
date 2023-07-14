class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        d = {}
        ln = len(arr)
        dp = [0] * (ln + 1)
        dp[ln - 1] = 1
        
        for i in range(ln - 1, -1, -1):
            if arr[i] + difference in d:
                val = arr[i] + difference
                dp[i] = dp[d[val]] + 1
            else:
                dp[i] = 1

            d[arr[i]] = i
                
        # print(dp)
        return max(dp)
    