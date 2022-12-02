class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        '''
        Time Complexity: O(N + M)
        Space Complexity: O(N + M)
        '''
        d1 = Counter(word1)
        d2 = Counter(word2)
        
        return d1.keys() == d2.keys() and sorted(d1.values()) == sorted(d2.values())
    