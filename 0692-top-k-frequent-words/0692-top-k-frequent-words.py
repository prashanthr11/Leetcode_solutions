class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return self.method_1(words, k)
    
    
    def method_1(self, words, k):
        '''
        Time Complexity: O(N logK)
        Space Complexity: O(N)
        '''
        d = Counter(words)
        lst = []
        
        for key, v in d.items():
            heappush(lst, (-v, key))
        

        return [i[1] for i in nsmallest(k, lst)]
    
    def method_2(self, words, k):
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(N)
        '''
        d = Counter(words)
        
        sorted_items = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        
        return [sorted_items[i][0] for i in range(k)]
    