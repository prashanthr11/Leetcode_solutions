class Solution:
    def reverseWords(self, s: str) -> str:
        return self.optimise(s)
    
    def naive(self, s):
        return " ".join(s.split()[::-1])
    
    def swap(self, lst):
        i, ln = 0, len(lst) - 1
        
        while i < ln:
            lst[i], lst[ln] = lst[ln], lst[i]
            i += 1
            ln -= 1

        return lst
    
    def custom_strip(self, lst):
        i, j, ln = 0, 0, len(lst)
        last_i = -1
        
        while j < ln:
            while j < ln and lst[j] == " ":
                j += 1
            
            if j < ln and last_i == i:
                lst[i] = " "
                i += 1
                
            while j < ln and lst[j] != " ":
                lst[i] = lst[j]
                i += 1
                j += 1
                last_i = i
            
        return lst[:i]
    
    def optimise(self, s):
        lst = list(map(str, s))
        lst = self.swap(lst)
        lst = self.custom_strip(lst)
        
        i, j, ln = 0, 0, len(lst)
        # print("".join(lst), len("".join(lst)), len("".join(lst).strip()))
        while j < ln:
            while j < ln and lst[j] != " ":
                j += 1
            
            tmp = j
            j -= 1
                
            while j < ln and i < j:
                lst[i], lst[j] = lst[j], lst[i]
                i += 1
                j -= 1
                
            i = tmp + 1
            while tmp < ln and lst[tmp] == " ":
                tmp += 1
                
            j = tmp
            
        return "".join(lst)
                
            