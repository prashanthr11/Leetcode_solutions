class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        Time Complexity: O(M + N) where M and N are lengths of the given strings
        Space Complexity: O(M)
        '''
        lst = defaultdict(int)
        ref = defaultdict(int)
        
        for i in t:
            lst[i] += 1
            ref[i] += 1
            
        i, ln = 0, len(s)
        cnt = len(t)
        mini = float('inf')
        j = 0
        
        while j < ln:
            while j < ln and cnt > 0:
                tmp = s[j]
                
                if lst[tmp] > 0:
                    cnt -= 1
                    
                if ref[tmp]:
                    lst[tmp] -= 1
                    
                j += 1
            
            while i < ln and cnt == 0:
                if mini > j - i:
                    mini = j - i
                    start = i
                
                char = s[i]
                
                if ref[char]:
                    if lst[char] == 0:
                        cnt += 1
                        
                    lst[char] += 1
                    
                i += 1
                
        return s[start: start + mini] if mini != float('inf') else ""
    