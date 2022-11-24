class Solution:
    def exist(self, a, word):
        
        # Time: O(N * M) Where N and M are elements in the board and length of the word respectively.
        # Space: O(N)
        
        def solve(r, c, s, idx, visited):
            nonlocal a

            if len(s) <= idx:
                return True

            neighbours = [(0, -1), (0, 1), (1, 0), (-1, 0)]

            for x, y in neighbours:
                if 0 <= x + r < len(a) and 0 <= y + c < len(a[0]):
                    if not visited[x + r][y + c] and a[x + r][y + c] == s[idx]:
                        visited[x + r][y + c] = True
                        if solve(x + r, y + c, s, idx + 1, visited):
                            return True
                        visited[x + r][y + c] = False

            return False

        visited = [[False] * len(a[0]) for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(a[0])):
                if a[i][j] == word[0]:
                    visited[i][j] = True
                    if solve(i, j, word, 1, visited):
                        return True
                    visited[i][j] = False
        
        return False