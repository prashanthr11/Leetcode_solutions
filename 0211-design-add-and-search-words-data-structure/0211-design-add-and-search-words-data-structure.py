class Trie:
    
    def __init__(self):
        self.nodes = defaultdict(dict)
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.trie_obj = Trie()
        

    def addWord(self, word: str) -> None:
        root = self.trie_obj
        
        for char in word:
            if char not in root.nodes:
                root.nodes[char] = Trie()
                
            root = root.nodes[char]
        
        root.is_end = True
        

    def search(self, word: str, root=None) -> bool:
        root = self.trie_obj if root is None else root
        
        for i, char in enumerate(word):
            if char != ".":
                if char not in root.nodes:
                    return False
                
                root = root.nodes[char]
            else:
                for char, node_ref in root.nodes.items():
                    if self.search(word[i + 1:], node_ref):
                        return True
                    
                return False
                    
        return root.is_end


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)