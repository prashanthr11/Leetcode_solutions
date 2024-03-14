class Solution:
    def minimumLength(self, s: str) -> int:
        return self.naive(s)
        
    def naive(self, s):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        l = deque(map(str, s))
        
        while len(l) > 1:
            top = l[0]
            ln = len(l)
            flag = False
            
            while l and l[-1] == top:
                l.pop()
                flag = True
                
            while l and flag and l[0] == top:
                l.popleft()
                
            if ln == len(l):
                break
                
        return len(l)
    