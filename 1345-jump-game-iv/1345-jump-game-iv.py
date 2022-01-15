class Solution:
    def minJumps(self, arr: List[int]) -> int:

        if len(arr) == 1:
            return 0
    
        self.store_indices(arr)
        n = len(arr)
        self.dp = [i for i in range(n)]
        return self.solve(arr, n)
        
        
    def store_indices(self, l):
        self.d = defaultdict(list)
        for i, a in enumerate(l):
            self.d[a].append(i)
            
       
    def solve(self, l, n):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        visited = [False] * n
        visited[0] = True
        q = [0]
        cnt = 0
        
        while q:
            tmp = []
            # print(q)
            for i in q:
                if i == n - 1:
                    return cnt

                for j in self.d[l[i]]:
                    if not visited[j]:
                        tmp.append(j)
                        visited[j] = True
                        
                self.d[l[i]] = []

                if i + 1 < n and not visited[i + 1]:
                    visited[i + 1] = True
                    tmp.append(i + 1)

                if i - 1 >= 0 and not visited[i - 1]:
                    visited[i - 1] = True
                    tmp.append(i - 1)

            q = tmp
            cnt += 1