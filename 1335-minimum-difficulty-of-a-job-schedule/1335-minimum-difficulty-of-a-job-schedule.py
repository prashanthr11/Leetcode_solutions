class Solution:
    def minDifficulty(self, jobDifficulty: List[int], d: int) -> int:
        self.jobs = jobDifficulty
        self.memo = {}
        ans = self.solve(0, d)
        
        return ans if ans != float('inf') else -1

    def solve(self, i, d):
        jobs = self.jobs
        
        if i == len(jobs) and d == 0:
            return 0
        
        if i >= len(jobs) or d <= 0:
            return float('inf')
        
        if (i, d) in self.memo:
            return self.memo[(i, d)]
        
        maxi = float('-inf')
        mini = float('inf')
        ret = mini
        
        for j in range(i, len(jobs)):
            maxi = max(maxi, jobs[j])
            inc = self.solve(j + 1, d - 1)
            not_inc = self.solve(j + 1, d)
            
            mini = min(mini, inc, not_inc)
                
            ret = min(ret, mini + maxi)
            
        self.memo[(i, d)] = ret
        return ret
