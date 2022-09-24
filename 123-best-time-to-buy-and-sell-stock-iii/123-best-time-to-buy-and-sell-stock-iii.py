class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        return self.even_optimise(prices, 2)
    
        return self.optimise(prices, 2)
    
        self.memo = defaultdict(int)
        return self.memoization(0, 2, prices, 0)

                
    def naive(self, trans_no, k, prices, i):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        if i >= len(prices) or trans_no > 2*k:
            return 0
                
        if trans_no % 2:
            return max(prices[i] + self.naive(trans_no + 1, k, prices, i + 1),
            self.naive(trans_no, k, prices, i + 1))
        else:
            return max(-prices[i] + self.naive(trans_no + 1, k, prices, i + 1),
            self.naive(trans_no, k, prices, i + 1))

    
    def memoization(self, trans_no, k, prices, i):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        if i >= len(prices) or trans_no > 2*k:
            return 0
        
        if (i, trans_no) in self.memo:
            return self.memo[(i, trans_no)]
        
        if trans_no % 2:
            self.memo[(i, trans_no)] = max(prices[i] + self.memoization(trans_no + 1, k, prices, i + 1),
            self.memoization(trans_no, k, prices, i + 1))
        else:
            self.memo[((i, trans_no))] = max(-prices[i] + self.memoization(trans_no + 1, k, prices, i + 1),
            self.memoization(trans_no, k, prices, i + 1))
            
        return self.memo[(i, trans_no)]
    
       
    def optimise(self, prices, k):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        n = len(prices)
        k *= 2
        dp = [[0]*(k + 1) for i in range(n + 1)]
        
        for i in range(n - 1, -1, -1):
            for j in range(k):
                if j % 2:
                    dp[i][j] = max(prices[i] + dp[i + 1][j + 1], dp[i + 1][j])
                else:
                    dp[i][j] = max(-prices[i] + dp[i + 1][j + 1], dp[i + 1][j])

        return dp[0][0]
    
    def even_optimise(self, prices, k):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        n = len(prices)
        k *= 2
        prev = [0] * (k + 1)
        cur = [0] * (k + 1)
        
        for i in range(n - 1, -1, -1):
            for j in range(k):
                if j % 2:
                    cur[j] = max(prices[i] + prev[j + 1], prev[j])
                else:
                    cur[j] = max(-prices[i] + prev[j + 1], prev[j])
            
            prev = cur
        
        return prev[0]
