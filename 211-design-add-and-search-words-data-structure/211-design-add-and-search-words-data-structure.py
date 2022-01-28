class Trie:
    def __init__(self, n=26, isEnd=False):
        self.lst = [None] * n
        self.isEnd = isEnd

class WordDictionary:

    def __init__(self):
        self.trie = Trie()

    def addWord(self, word: str) -> None:
        trie_copy = self.trie
        for i in word:
            ascii = ord(i) - ord('a')
            if trie_copy.lst[ascii] is None:
                trie_copy.lst[ascii] = Trie()
                
            trie_copy = trie_copy.lst[ascii]
            
        trie_copy.isEnd = True

    def search(self, word: str) -> bool:
        return self.search_rec(self.trie, word)
    
    def search_rec(self, trie_copy, word):
        
        for i in range(len(word)):
            if word[i] == '.':
                for j in trie_copy.lst:
                    if j:
                        if self.search_rec(j, word[i + 1:]):
                            return True
                        
                return False
            else:
                if trie_copy.lst[ord(word[i]) - ord('a')]:
                    trie_copy = trie_copy.lst[ord(word[i]) - ord('a')]
                else:
                    return False
                
        return trie_copy.isEnd

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)