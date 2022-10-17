class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        l = [0] * 26
        
        for i in sentence:
            l[ord(i) - ord('a')] += 1
            
        for i in l:
            if not i:
                return False
            
        return True
    