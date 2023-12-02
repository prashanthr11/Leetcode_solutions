class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        ret = 0
        
        d = Counter(chars)
        
        for word in words:
            word_cntr = Counter(word)
            
            if len(word_cntr - d) == 0:
                ret += len(word)
                
        return ret
    