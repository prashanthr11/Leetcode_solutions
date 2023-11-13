class Solution:
    def sortVowels(self, s: str) -> str:
        vowel_strs = [i for i in s if i in 'aeiouAEIOU']
        vowel_strs.sort()
        pos = 0
        s = list(s)
        
        for i in range(len(s)):
            if s[i] in 'aeiouAEIOU':
                s[i] = vowel_strs[pos]
                pos += 1
                
        return "".join(s)
    