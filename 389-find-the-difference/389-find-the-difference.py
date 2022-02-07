class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        '''
        Time Complexity: O(N) where N is the lenght of t
        Space Complexity: O(1)
        '''
        counts = [0] * 26
        
        for i in t:
            counts[ord(i) - ord('a')] += 1
            
        for i in s:
            counts[ord(i) - ord('a')] -= 1
            
        for i, a in enumerate(counts):
            if a:
                return chr(ord('a') + i)
            