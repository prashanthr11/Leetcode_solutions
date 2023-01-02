class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return self.optimise(word)
        
    def optimise(self, word):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        def solve_all_small(word, low=0):
            for i, s in enumerate(word[low:]):
                if ord('A') <= ord(s) <= ord('Z'):
                    return False
            
            return True
        
        def solve_all_capital():
            for s in word:
                if ord('a') <= ord(s) <= ord('z'):
                    return False
                
            return True
        
        if ord('a') <= ord(word[0]) <= ord('z'):
            return solve_all_small(word)
        else:
            if len(word) <= 1:
                return True
            
            if ord('a') <= ord(word[1]) <= ord('z'):
                return solve_all_small(word, low=1)
            
            return solve_all_capital()
        
    def naive(self, word):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        return word.upper() == word or word.lower() == word or word.capitalize() == word
    
        