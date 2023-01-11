class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        def dfs(cur, parent):
            ret =  0
            
            for child in d[cur]:
                if child == parent:
                    continue
                    
                tmp = dfs(child, cur)
                
                if tmp or hasApple[child]:
                    ret += tmp + 2
                    
            return ret
        
        d = defaultdict(list)
        for u, v in edges:
            d[u].append(v)
            d[v].append(u)
            
        return dfs(0, -1)
    