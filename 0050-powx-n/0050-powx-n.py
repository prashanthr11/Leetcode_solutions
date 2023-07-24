class Solution:
    def myPow(self, x: float, n: int) -> float:
        
        if n == 0:
            return 1
        
        d = {}
        
        d[0] = 1
        d[1] = x if n > 0 else 1/x
        i = 2
        max_power = abs(n)
        powers = [0, 1]
        
        while i <= max_power:
            d[i] = d[i >> 1] ** 2
            powers.append(i)
            i <<= 1
            
        def solve(n):
            idx = bisect_left(powers, n)
            if idx >= len(powers):
                return d[powers[idx - 1]] * solve(n - powers[idx - 1])
            else:
                if powers[idx] == n:
                    return d[powers[idx]]
                else:
                    return d[powers[idx - 1]] * solve(n - powers[idx - 1])
        
        return solve(max_power)
        