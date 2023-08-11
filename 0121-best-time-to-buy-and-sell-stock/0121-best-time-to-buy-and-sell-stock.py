class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxi = 0
        low = float('inf')
        
        for i in prices:
            low = min(low, i)
            maxi = max(maxi, i - low)
            
        return maxi
    