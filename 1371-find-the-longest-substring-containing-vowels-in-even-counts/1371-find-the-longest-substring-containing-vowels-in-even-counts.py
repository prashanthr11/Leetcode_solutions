class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        
        mp = {}
        mp[0] = -1
        prefix_xor = 0
        result = 0
        
        d = {
            'a': 5,
            'e': 1,
            'i': 2,
            'o': 3,
            'u': 4,
        }

        
        for i, char in enumerate(s):
            if char in d:
                prefix_xor ^= (1 << d[char])
                
            if prefix_xor not in mp:
                mp[prefix_xor] = i
                
            result = max(result, i - mp[prefix_xor])
                
        return result
    