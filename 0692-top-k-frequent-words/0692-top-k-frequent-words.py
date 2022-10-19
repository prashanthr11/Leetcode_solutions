class TrieNode:
    def __init__(self):
        self.lst = [None] * 26
        self.is_end = [False] * 26
        

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        return self.method_3(words, k)
    
    
    def method_1(self, words, k):
        '''
        Time Complexity: O(N logK)
        Space Complexity: O(N)
        '''
        d = Counter(words)
        lst = []
        
        for key, v in d.items():
            heappush(lst, (-v, key))
        

        return [i[1] for i in nsmallest(k, lst)]
    
    def method_2(self, words, k):
        '''
        Time Complexity: O(N logN)
        Space Complexity: O(N)
        '''
        d = Counter(words)
        
        sorted_items = sorted(d.items(), key=lambda x: (-x[1], x[0]))
        
        return [sorted_items[i][0] for i in range(k)]
    
    def method_3(self, words, k):
        '''
        Using bucket sort
        Time Complexity: O(N*W*L) where W and L are no of words and avg length of the words respectively
        Space Complexity: O(N)
        '''
        
        d = Counter(words)
        ln = len(words)
        ret = []
        
        bucket = [set() for i in range(ln + 1)]
        
        for key, v in d.items():
            bucket[v].add(key)
            
        for i in range(ln, -1, -1):
            if k == 0:
                break
                
            highest_freq_words = bucket[i]
            
            if len(highest_freq_words):
                root = self.build_trie(highest_freq_words)

                top_words = self.get_words(root, '')

                for i in top_words:
                    if k > 0:
                        ret.append(i)
                        k -= 1
                    else:
                        break
                    
        return ret
    
    def build_trie(self, words):
        root = TrieNode()
        
        for word in words:
            cur = root

            for char in word:
                idx = ord(char) - ord('a')

                if not cur.lst[idx]:
                    cur.lst[idx] = TrieNode()
                
                cur = cur.lst[idx]
                
            cur.is_end[idx] = True
                
        return root
    
    def get_words(self, root, word):
        ret = []
        
        for i in range(26):
            if root.is_end[i]:
                ret.append(word)
                
            if root.lst[i]:
                ret += self.get_words(root.lst[i], word + chr(ord('a') + i))
                
        return ret
    