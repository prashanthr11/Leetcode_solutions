class Solution:
    def minDeletions(self, s: str) -> int:
        lst = sorted(Counter(s).values())
        ret = 0
        st = set([lst[0]])
        
        for i in range(1, len(lst)):
            if lst[i] - lst[i - 1] == 0:
                j = lst[i - 1]
                while j > 0 and j in st:
                    j -= 1
                    
                ret += (lst[i] - j)
                st.add(j)
            else:
                st.add(lst[i])
            
        return ret
    