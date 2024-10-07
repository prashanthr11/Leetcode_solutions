class TrieNode:

    def __init__(self):
        self.chars = [None] * 26
        self.is_end = False


class WordDictionary:

    def __init__(self):
        self.head = TrieNode()

    def addWord(self, word):
        trie_ref = self.head

        for char in word:
            idx = ord(char) - ord('a')

            if not trie_ref.chars[idx]:
                trie_ref.chars[idx] = TrieNode()

            trie_ref = trie_ref.chars[idx]

        trie_ref.is_end = True


    def search(self, word):
        return self.dfs(self.head, word)


    def dfs(self, trie_ref, word):
        for i, char in enumerate(word):
            if char == '.':
                for child in trie_ref.chars:
                    if child:
                        if self.dfs(child, word[i + 1:]):
                            return True
                return False
            else:
                idx = ord(char) - ord('a')

                if trie_ref.chars[idx] is None:
                    return False

                trie_ref = trie_ref.chars[idx]

        return trie_ref.is_end