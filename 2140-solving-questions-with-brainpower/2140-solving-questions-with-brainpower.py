class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        ln = len(questions)
        dp = [0] * ln
        dp[-1] = questions[-1][0]
        
        for i in range(ln - 2, -1, -1):
            tmp = 0 if questions[i][1] + i + 1 >= ln else dp[i + 1 + questions[i][1]]
            maxi = max(dp[i + 1], questions[i][0] + tmp)
            dp[i] = maxi
            
        # print(dp)
        return dp[0]
