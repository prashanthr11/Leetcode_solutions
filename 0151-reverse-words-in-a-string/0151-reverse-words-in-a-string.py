class Solution:
    def reverseWords(self, s: str) -> str:
        return self.naive(s)
    
    def naive(self, s):
        return " ".join(s.split()[::-1])
    