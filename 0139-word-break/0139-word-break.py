class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        ln = len(s)
        dp = defaultdict(lambda : False)
        dp[0] = True
        
        for i in range(1, ln + 1):
            for word in wordDict:
                word_ln = len(word)
                
                if word_ln > i:
                    continue
                    
                if dp[i - word_ln] and s[i - word_ln:i] == word:
                    dp[i] = True
                    break

        return dp[ln]
    