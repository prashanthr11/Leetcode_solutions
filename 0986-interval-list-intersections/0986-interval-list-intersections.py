class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ret = []
        
        i, j, n, m = 0, 0, len(firstList), len(secondList)
        
        while i < n and j < m:
            
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            
            if start <= end:
                ret.append([start, end])
            
            if end == firstList[i][1]:
                i += 1
            else:
                j += 1
                
        return ret
    