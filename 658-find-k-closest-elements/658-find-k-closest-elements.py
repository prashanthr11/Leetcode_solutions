class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect(arr, x)
        ret = deque([])
        right, left = idx, idx - 1
        ln = len(arr)
        
        while k > 0:
            if left >= 0 and right < ln:
                if abs(arr[left] - x) <= abs(arr[right] - x):
                    ret.appendleft(arr[left])
                    left -= 1
                else:
                    ret.append(arr[right])
                    right += 1
                    
                k -= 1
            else:
                if left >= 0:
                    ret.appendleft(arr[left])
                    left -= 1
                    k -= 1
                    
                if right < ln:
                    ret.append(arr[right])
                    k -= 1
                    right += 1
                    
        return ret
    