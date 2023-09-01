class Solution:
    def countBits(self, n: int) -> List[int]:
        def solve(x):
            cnt = 0
            while x:
                cnt += (1 if x&1 else 0)
                x >>= 1
                
            return cnt
        
        return [solve(i) for i in range(n + 1)]
