class Solution:
    def findOriginalArray(self, changed: List[int]) -> List[int]:
        return self.naive(changed)
    
    def naive(self, changed):
        '''
        Time Complexity: O(N log N)
        Space Complexity: O(N)
        '''
        ret = []
        
        if len(changed) % 2:
            return ret
        
        sorted_changed = sorted(changed)

        d = Counter(changed)

        for i in sorted_changed[::-1]:
            if d[i] > 0:
                if i % 2 == 0 and d[i // 2] > 0:
                    d[i] -= 1
                    d[i // 2] -= 1
                    ret.append(i//2)
                else:
                    return []
        return ret
    