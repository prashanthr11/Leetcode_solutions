class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        ln = len(prices)
        memo = {}
        
        def dp(idx, need_to_buy):
            
            if idx >= ln:
                return 0
            
            if (idx, need_to_buy) in memo:
                return memo[(idx, need_to_buy)]
            
            maxi = 0
            if need_to_buy:
                maxi = max(-prices[idx] + dp(idx + 1, False), dp(idx + 1, True))
            else:
                maxi = max(prices[idx] - fee + dp(idx + 1, True), dp(idx + 1, False))
            
            memo[(idx, need_to_buy)] = maxi
            return maxi
        
        return dp(0, True)
    