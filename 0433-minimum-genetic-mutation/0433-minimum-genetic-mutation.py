class state:
    def __init__(self, g_of_n, word, end):
        self.g_of_n = g_of_n
        self.word = word
        self.h_of_n = self.calculate_heuristic(word, end)
        self.cost = self.h_of_n + g_of_n
        
    def calculate_heuristic(self, word, end):
        i, j, n, m = 0, 0, len(word), len(end)
        cnt = 0
        
        while i < n and j < m:
            cnt += word[i] != end[j]
            i += 1
            j += 1
            
        return cnt
    
    def __lt__(self, other):
        return self.cost < other.cost

class AStar:
    def is_successor(self, word1, word2):
        i, j, n, m = 0, 0, len(word1), len(word2)
        cnt = 0

        while i < n and j < m:
            if word1[i] != word2[j]:
                cnt += 1

            i += 1
            j += 1

        return cnt + (i - n) + (j - m) == 1

    def successors(self, strt, bank):
        ret = []
        for word in bank:
            if self.is_successor(word, strt):
                ret.append(word)

        return ret
    
    def solve(self, start, end, bank):
        dq = [state(0, start, end)]
        
        visited = set()
        while len(dq):
            state_obj = heappop(dq)
            
            if state_obj.word == end:
                return state_obj.cost
            
            if state_obj.word in visited:
                continue
                
            visited.add(state_obj.word)
            
            for i in self.successors(state_obj.word, bank):
                if i not in visited:
                    heappush(dq, state(state_obj.g_of_n + 1, i, end))
                    
        return -1


class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        return AStar().solve(start, end, bank)
     