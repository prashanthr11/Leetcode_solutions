class Trie:
    
    def __init__(self):
        self.nodes = [None] * 26
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.trie_obj = Trie()
        

    def addWord(self, word: str) -> None:
        root = self.trie_obj
        
        for char in word:
            idx = ord(char) - ord('a')
            if not root.nodes[idx]:
                root.nodes[idx] = Trie()
                
            root = root.nodes[idx]
        
        root.is_end = True
        

    def search(self, word: str, root=None) -> bool:
        root = self.trie_obj if root is None else root
        
        for i, char in enumerate(word):
            if char != ".":
                idx = ord(char) - ord('a')
                
                if not root.nodes[idx]:
                    return False
                
                root = root.nodes[idx]
            else:
                for node in root.nodes:
                    if node and self.search(word[i + 1:], node):
                        return True
                    
                return False
                    
        return root.is_end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)