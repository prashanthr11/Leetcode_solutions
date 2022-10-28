class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(N)
        '''
        d = defaultdict(list)
        
        for i in strs:
            d[tuple(sorted(map(str, i)))].append(i)
            
        return list(d.values())
    