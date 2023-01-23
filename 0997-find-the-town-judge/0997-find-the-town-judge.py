class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        inbound = [0] * n
        outbound = [0] * n
        
        for a, b in trust:
            inbound[b - 1] += 1
            outbound[a - 1] += 1
            
        for i in range(n):
            if inbound[i] == n - 1 and outbound[i] == 0:
                return i + 1
            
        return -1
    