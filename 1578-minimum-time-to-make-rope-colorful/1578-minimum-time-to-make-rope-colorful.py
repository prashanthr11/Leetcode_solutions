class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:

        ln = len(colors)
        prev_idx = -1
        ret = 0
        i = 0
        
        while i < ln:
            tmp = [neededTime[i]]
            j = i + 1
            while j < ln:
                if colors[i] == colors[j]:
                    tmp.append(neededTime[j])
                else:
                    break
                j += 1
                    
            if len(tmp) > 1:
                ret += sum(sorted(tmp)[:-1])
                
            i = j
            
        return ret
    