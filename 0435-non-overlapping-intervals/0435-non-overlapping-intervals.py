class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        ln = len(intervals)
        dp = {}
        intervals.sort()
        cached_bs = [bisect_right(intervals, [end, float('-inf')]) for start, end in intervals]
        dp = [0] * (ln + 1)
        
        for i in range(ln - 1, -1, -1):
            dp[i] = max(dp[i + 1], 1 + dp[cached_bs[i]])
            
        return ln - dp[0]
#         def dfs(idx):
#             if idx >= ln:
#                 return 0
            
#             if idx in dp:
#                 return dp[idx]
            
#             maxi = 0
#             for i in range(idx, ln):
#                 maxi = max(maxi, 1 + dfs(cached_bs[i]))
                
#             dp[idx] = maxi
#             return maxi
        
#         return ln - dfs(0)
#         lst = [dfs(i) for i in range(ln)]
#         print(lst)
#         print(dp.items())
#         return ln - max(lst)