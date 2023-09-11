class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        '''
        TC: O(N)
        SC: O(N)
        '''
        dt = defaultdict(list)
        
        for i, size in enumerate(groupSizes):
            dt[size].append(i)
            
        ret = []
        for k, v in dt.items():
            for i in range(0, len(v), k):
                ret.append(v[i:i + k])
        
        return ret
    