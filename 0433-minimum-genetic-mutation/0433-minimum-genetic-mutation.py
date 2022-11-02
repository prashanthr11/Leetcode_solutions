class Solution:
    def minMutation(self, start: str, end: str, bank: List[str]) -> int:
        return self.naive(start, end, bank)
    
    def naive(self, start, end, bank):
        def is_successor(a, b):
            i, j, n, m = 0, 0, len(a), len(b)
            cnt = 0
            
            while i < n and j < m:
                if a[i] != b[j]:
                    cnt += 1
                    
                i += 1
                j += 1
                
            return cnt + (i - n) + (j - m) == 1
        
        def successors(strt):
            ret = []
            for word in bank:
                if is_successor(word, strt):
                    ret.append(word)
                    
            return ret
        
        dq = deque([(start, [], 0)])
        
        while dq:
            top, visited, cnt = dq.popleft()
            
            if top == end:
                return cnt
            
            for i in successors(top):
                if i not in visited:
                    dq.append((i, visited + [top], cnt + 1))
                    
        return -1
    