class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        ln1, ln2 = len(nums1), len(nums2)
        ret = []
        pq = [(nums1[0] + nums2[0], 0, 0)]
        visited = set()
        
        while k and pq:
            val, x, y = heappop(pq)
            if (x, y) in visited:
                continue
            
            visited.add((x, y))
            ret.append([nums1[x], nums2[y]])
            
            if x + 1 < ln1:
                heappush(pq, (nums2[y] + nums1[x + 1], x + 1, y))
                
            if y + 1 < ln2:
                heappush(pq, (nums1[x] + nums2[y + 1], x, y + 1))
                
            k -= 1
            
        return ret
