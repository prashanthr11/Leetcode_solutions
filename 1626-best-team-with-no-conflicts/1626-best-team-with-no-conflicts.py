class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        return self.naive(scores, ages)
    
    def naive(self, scores, ages):
        ln = len(ages)
        lst= [(ages[i], scores[i]) for i in range(ln)]
        lst.sort()
        
        dp = [score for age, score in lst]
        
        for i in range(ln):
            for j in range(i - 1, -1, -1):
                if lst[j][1] <= lst[i][1]:
                    dp[i] = max(dp[i], lst[i][1] + dp[j])
                    
        return max(dp)