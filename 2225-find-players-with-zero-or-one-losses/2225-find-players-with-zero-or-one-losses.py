class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        return self.naive(matches)

    def naive(self, matches):
        wins = defaultdict(int)
        loss = defaultdict(int)
        
        st = set()
        first = set()
        second = set()
        
        for a, b in matches:
            wins[a] += 1
            loss[b] += 1
            st.add(a)
            st.add(b)
        
        for i in st:
            losses = loss[i]
            
            if losses == 0:
                first.add(i)
            elif losses == 1:
                second.add(i)
                
        return [sorted(first), sorted(second)]
        