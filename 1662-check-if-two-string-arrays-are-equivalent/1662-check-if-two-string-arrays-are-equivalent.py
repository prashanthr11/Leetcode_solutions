class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        '''
        Time Complexity = O(N + M)
        Space Complexity = O(1)
        '''
        i_pos = j_pos = i = j = 0
        n, m = len(word1), len(word2)
        
        while i < n and j < m:    
            while i_pos < len(word1[i]) and j_pos < len(word2[j]):
                if word1[i][i_pos] != word2[j][j_pos]:
                    return False
                
                i_pos += 1
                j_pos += 1
                
            if i_pos == len(word1[i]):
                i += 1
                i_pos = 0
                
            if j_pos == len(word2[j]):
                j += 1
                j_pos = 0
                
        return i == n and j == m
    