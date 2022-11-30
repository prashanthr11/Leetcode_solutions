class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        return self.naive(arr)
    
    def naive(self, arr):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        d = Counter(arr)
            
        return len(d) == len(set(d.values()))
    