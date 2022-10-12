class Solution:
    def pushDominoes(self, dominoes: str) -> str:
        ln = len(dominoes)
        powers = [0] * ln
        
        for i in range(ln):
            if dominoes[i] == "R":
                powers[i] = ln
            elif dominoes[i] == "L":
                powers[i] = 0
            else:
                powers[i] = max(powers[i - 1] - 1, 0)
                
        f = 0
        for i in range(ln - 1, -1, -1):
            if dominoes[i] == "L":
                f = ln
            elif dominoes[i] == "R":
                f = 0
            else:
                f = max(f - 1, 0)
                
            powers[i] -= f
    
        return "".join("." if i == 0 else "L" if i < 0 else "R" for i in powers)
    