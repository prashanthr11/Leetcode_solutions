class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        d = defaultdict(list)
        indegree = [0] * numCourses
        ret = []
        
        for x, y in prerequisites:
            d[y].append(x)
            indegree[x] += 1
            
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        
        while queue:
            top = queue.popleft()
            ret.append(top)
            
            for nei in d[top]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        return [] if len(ret) != numCourses else ret
    