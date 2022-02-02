class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        return self.optimised(s, p)
        
        
    def naive_modified(self, s, p):
        def _check(s, l):
            return tmp == l
        
        chars = [0] * 26
        tmp = [0] * 26
        ret = []
        
        for i in p:
            chars[ord(i) - ord('a')] += 1
        
        ln = len(p)
        for i in range(len(s) - ln + 1):
            for j in s[i:i + ln]:
                tmp[ord(j) - ord('a')] += 1
                
            if _check(s[i:i + ln], chars):
                ret.append(i)
                
            for j in s[i:i + ln]:
                tmp[ord(j) - ord('a')] -= 1
                
        return ret
    
    
    def optimised(self, s, p):
        ret = list()
        window = len(p)
        count = [0] * 26
        
        for i in p:
            count[ord(i) - ord('a')] += 1
            
        unq = sum([1 for i in count if i])

        filtered_s = list()
        for i, a in enumerate(s):
            if count[ord(a) - ord('a')]:
                filtered_s.append((i, a))
                
        i = 0
        j = i
        n = len(filtered_s)
        cur_unq = 0
        
        while i < n:
                
            while j < n and cur_unq != unq:
                char = filtered_s[j][1]
                count[ord(char) - ord('a')] -= 1
                if count[ord(char) - ord('a')] == 0:
                    cur_unq += 1
                    
                j += 1

            end = filtered_s[j - 1][0]

            while i <= j and i < n and cur_unq == unq:
                start = filtered_s[i][0]
                if end - start + 1 == window:
                    ret.append(start)

                char = filtered_s[i][1]
                count[ord(char) - ord('a')] += 1
                if count[ord(char) - ord('a')] > 0:
                    cur_unq -= 1

                i += 1
                
            if j == n:
                break
                    
        return ret
                
            
    def naive(self, s, p):
        def check(a, b):
            return a == b
        
        d1 = Counter(p)
        ret = []
        ln = len(p)
        
        for i in range(len(s) - ln + 1):
            if check(Counter(s[i:i + ln]), d1):
                ret.append(i)
                
        return ret
    