class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        return self.naive(tasks)
    
    def naive(self, tasks):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        dp = [float('inf')] * (10**5 + 1)
        
        dp[2] = dp[3] = 1
        
        for i in range(4, 10**5 + 1):
            dp[i] = min(dp[i - 2], dp[i - 3]) + 1
            
        d = Counter(tasks)
        st = list(d.values())
        cnt = 0
        
        for i in st:
            if dp[i] == float('inf'):
                return -1
            
            cnt += dp[i]
            
        return cnt
    