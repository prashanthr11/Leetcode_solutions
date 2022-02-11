class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return self.solve(s1, s2)

    def naive(self, s1, s2):
        '''
        Time Complexity: O(M*N) where N and M are the lenghts of the given strings b and a respectively.
        Space Complexity: O(N)
        '''
        ln = len(s1)
        d = Counter(s1)
        for i in range(len(s2) - ln + 1):
            if self.compare(d, s2[i:i + ln]):
                return True
            
        return False
    
    def compare(self, a, b):
        '''
        Time Complexity: O(N + M) where N and M are the lenghts of the given strings.
        Space Complexity: O(N + M)
        
        '''
        return len(Counter(b) - a) == 0
    
    def solve(self, s1, s2):
        '''
        Time Complexity: O(N + M)
        Space Complexity: O(1)
        '''
        ln = len(s1)
        char_counts = [0] * 26
        
        for i in s1:
            char_counts[ord(i) - ord('a')] += 1
            
        for i in range(len(s2) - ln + 1):
            if self.are_equal(char_counts.copy(), s2[i:i + ln]):
                return True
            
        return False
    
    def are_equal(self, l, s):
        for a, i in enumerate(s):
            if l[ord(i) - ord('a')] <= 0:
                return False
            
            l[ord(i) - ord('a')] -= 1
            
        return len([i for i in l if i != 0]) == 0
    