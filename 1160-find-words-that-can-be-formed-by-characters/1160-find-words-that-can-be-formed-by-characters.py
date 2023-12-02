class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ret = 0
        d = [0] * 26
        
        for i in chars:
            d[ord(i) - ord('a')] += 1
        
        for word in words:
            d_copy = d.copy()
            flag = True
            
            for j in word:
                if d_copy[ord(j) - ord('a')] <= 0:
                    flag = False
                    break
                    
                d_copy[ord(j) - ord('a')] -= 1
                
            if flag:
                ret += len(word)
            
        return ret
    