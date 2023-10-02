class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        alise = 0
        bob = 0
        
        for i in range(1, len(colors) - 1):
            if colors[i] == colors[i - 1] == colors[i + 1]:
                if colors[i] == 'A':
                    alise += 1
                elif colors[i] == 'B':
                    bob += 1
                
        return alise > bob
    