class Solution:
    def canPlaceFlowers(self, l: List[int], n: int) -> bool:
        i, ln, cnt = 0, len(l), 0
        
        while i < ln:
            if i == 0:
                if l[i] == 0:
                    if i + 1 < ln:
                        if l[i + 1] == 0:
                            l[i] = 1
                            cnt += 1
                    else:
                        l[i] = 1
                        cnt += 1
            elif i == ln - 1:
                if l[i] == 0:
                    if i - 1 >= 0:
                        if l[i - 1] == 0:
                            l[i] = 1
                            cnt += 1
                    else:
                        l[i] = 1
                        cnt += 1
            else:
                if l[i] == l[i - 1] == l[i + 1] == 0:
                    l[i] = 1
                    i += 1
                    cnt += 1
                    
            i += 1
            
        return cnt >= n