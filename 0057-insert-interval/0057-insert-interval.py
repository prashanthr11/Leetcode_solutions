class Solution:
    def insert(self, a: List[List[int]], b: List[int]) -> List[List[int]]:
        
        # Time: O(N LogN)
        # Space: O(N)
        
        if not a:
            return [b]
        
        idx = bisect.bisect(a, b[0], key=lambda x:x[0])
        a.insert(idx, b)
        ret = list()
        
        mini, maxi = a[0][0], a[0][1]
        
        for i in range(1, len(a)):
            if maxi >= a[i][0]:
                maxi = max(maxi, a[i][1])
                mini = min(mini, a[i][0])
            else:
                ret.append([mini, maxi])
                mini = a[i][0]
                maxi = a[i][1]
                
        ret.append([mini, maxi])
        return ret