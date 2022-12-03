class Solution:
    def frequencySort(self, s: str) -> str:
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(N)
        '''
        d = Counter(s)
        ret = [""] * sum(d.values())
        pos = 0
        
        for k, v in sorted(d.items(), key=lambda x:-x[1]):
            for i in range(v):
                ret[pos] = k
                pos += 1
            
        return ''.join(ret)
    