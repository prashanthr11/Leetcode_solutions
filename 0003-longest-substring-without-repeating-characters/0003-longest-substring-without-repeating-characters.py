class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left, right = 0, 0
        n = len(s)
        result = 0
        unique_chars = 0
        freq_map = defaultdict(int)
        
        while right < n:
            while right < n and freq_map[s[right]] == 0:
                freq_map[s[right]] = 1
                right += 1
                
            result = max(result, right - left)
            freq_map[s[left]] -= 1
            left += 1
            
        return result
