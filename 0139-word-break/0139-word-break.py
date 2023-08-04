class Trie:
    def __init__(self):
        self.l = [0] * 26
        self.is_end = [0] * 26
        
    def __repr__(self):
        return ''.join([chr(ord('a') + i) for i in range(26) if self.l[i]])

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie_obj = Trie()
        
        for word in wordDict:
            tmp_trie_obj = trie_obj
            prev = None
            for letter in word:
                if not tmp_trie_obj.l[ord(letter) - ord('a')]:
                    tmp_trie_obj.l[ord(letter) - ord('a')] = Trie()
                    
                prev_obj = tmp_trie_obj
                tmp_trie_obj = tmp_trie_obj.l[ord(letter) - ord('a')]
                prev = ord(letter) - ord('a')
                
            prev_obj.is_end[prev] = True
            
        queue = deque([(0, trie_obj)])
        ln_s = len(s)
        visited = set()
        
        while queue:
            # print(queue)
            top, trie_ref = queue.popleft()
            
            if top >= ln_s or (top, trie_ref) in visited:
                continue
                
            visited.add((top, trie_ref))
            
            ascii_value = ord(s[top]) - ord('a')
            
            if not trie_ref.l[ascii_value]:
                continue
            
            if trie_ref.is_end[ascii_value]:
                if top + 1 >= ln_s:
                    return True
                
                queue.append((top + 1, trie_obj))
            
            queue.append((top + 1, trie_ref.l[ascii_value]))
            
        return False
    