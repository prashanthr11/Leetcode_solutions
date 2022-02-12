class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        return self.optimise(beginWord, endWord, wordList)
        
    def naive(self, beginWord, endWord, wordList):
        if endWord not in wordList:
            return 0
        
        self.ans = float('inf')
        if beginWord not in wordList:
            wordList += [beginWord]
            
        self.solve(beginWord, endWord, [endWord], wordList)
        return self.ans if self.ans != float('inf') else 0
                
    def solve(self, beginWord, endWord, vis, wordList):
        if beginWord == endWord:
            print(vis)
            self.ans = min(self.ans, len(vis))
            return
        
        for i in wordList:
            if i not in vis and self.compare(endWord, i):
                self.solve(beginWord, i, vis + [i], wordList)
    
    def compare(self, a, b):
        flag = True
        
        for i in range(len(a)):
            if a[i] != b[i]:
                if flag:
                    flag = False
                else:
                    return flag
                
        return not flag
    
    def optimise(self, begin, end, words):
        if end not in words:
            return 0
        
        trie = self.buildTrie(words)
        q  = deque([(begin, 1)])
        vis = set([begin])
        while q:
            # print(q)
            top = q.popleft()
            if top[0] == end:
                return top[1]
            
            response = self.getWords(top[0], trie)
            # print(top[0], response)
            for i in response:
                if i not in vis:
                    vis.add(i)
                    q.append((i, top[1] + 1))
            '''
            for i in words:
                if i not in vis and self.compare(top[0], i):
                    q.append((i, top[1] + 1))
                    vis.add(i)
            '''        
        return 0
    
    def getWords(self, a, trie):
        ret = []
        for i in range(len(a)):
            ret += self.gett(a[:i] + '.' + a[i + 1:], trie, '')
            
        return set(ret)
    
    def buildTrie(self, words):
        trie = [None] * 26
        
        for word in words:
            tmp_trie = trie
            for i in word:
                if not tmp_trie[ord(i) - ord('a')]:
                    tmp_trie[ord(i) - ord('a')] = [None] * 26
                
                tmp_trie = tmp_trie[ord(i) - ord('a')]
                
        return trie
    
    def gett(self, s, trie, tmp):
        ret = []
        for i, a in enumerate(s):
            if a == '.':
                for j in range(26):
                    if trie[j]:
                        # print(s, j, chr(ord('a') + j))
                        ret += self.gett(s[i + 1:], trie[j], tmp + chr(ord('a') + j))
                
                return ret
            else:
                if trie[ord(a) - ord('a')]:
                    trie = trie[ord(a) - ord('a')]
                    tmp += a
                else:
                    return []
                    
        return [tmp]