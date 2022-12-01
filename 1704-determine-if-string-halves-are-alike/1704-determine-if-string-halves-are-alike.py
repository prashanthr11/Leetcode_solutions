class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        i, ln = 0, len(s) - 1
        cnt = 0
        vowels = "aeiouAEIOU"
        
        while i < ln:
            cnt += s[i] in vowels
            cnt -= s[ln] in vowels
            
            i += 1
            ln -= 1
            
        return cnt == 0
    