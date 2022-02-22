class Solution:
    def titleToNumber(self, s: str) -> int:
        ans = 0
        n = len(s)
        for i in range(n, 0, -1):
            ans += pow(26, n - i) * (ord(s[i - 1]) - ord('A') + 1)
        return ans
        