class Solution:
    def mostPopularCreator(self, creators: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        return self.optimise(creators, ids, views)
    
    def optimise(self, creators, ids, views):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        d = defaultdict(list)
        ln = len(ids)
        ret = []
        
        for i in range(ln):
            d[creators[i]].append((ids[i], views[i]))
            
        maxi = {}
        for k, v in d.items():
            maxi[k] = sum([i[1] for i in v])
        
        max_views = max(maxi.values())
        for k, v in maxi.items():
            if v == max_views:
                max_ = max([i[1] for i in d[k]])
                min_ = min([i[0] for i in d[k] if i[1] == max_])
                ret.append([k, min_])
                
        return ret
    
    def solve(self, creators, ids, views):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        maxis = defaultdict(int)
        cnt = defaultdict(int)
        minis = {}
        
        ln = len(creators)
        
        for i in range(ln):
            maxis[creators[i]] = max(maxis[creators[i]], views[i])
            cnt[creators[i]] += views[i]

        max_views = max(cnt.values())
        for i in range(ln):
            if cnt[creators[i]] == max_views and maxis[creators[i]] == views[i]:
                if creators[i] in minis:
                    minis[creators[i]] = min(minis[creators[i]], ids[i])
                else:
                    minis[creators[i]] = ids[i]
    
        ret = []
        for k, v in cnt.items():
            if v == max_views:
                ret.append([k, minis[k]])
                
        return ret
    