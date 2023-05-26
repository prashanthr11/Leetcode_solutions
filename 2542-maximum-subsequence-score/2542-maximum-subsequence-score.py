class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        lst = [(a, b) for a, b in zip(nums1, nums2)]
        lst.sort(key=lambda x:-x[1])
        
        top_k_scores = [i[0] for i in lst[:k]]
        heapify(top_k_scores)
        sumi = sum(top_k_scores)
        ans = sumi * lst[k - 1][1]
        
        for i in range(k, len(nums1)):
            sumi -= heappop(top_k_scores)
            sumi += lst[i][0]
            heappush(top_k_scores, lst[i][0])
            ans = max(ans, sumi * lst[i][1])
            
        return ans
    