class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for coin in coins:
            if coin > amount:
                continue
                
            dp[coin] += 1
            for i in range(coin + 1, amount + 1):
                if i - coin >= 0 and dp[i - coin] >= 0:
                    dp[i] += dp[i - coin]
                    
        return dp[amount]
