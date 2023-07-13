class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d = defaultdict(list)
        indegree = [0] * numCourses
        
        for x, y in prerequisites:
            d[y].append(x)
            indegree[x] += 1
            
        queue = deque([i for i in range(numCourses) if indegree[i] == 0])
        cnt = 0
        
        while queue:
            top = queue.popleft()
            cnt += 1
            
            for nei in d[top]:
                indegree[nei] -= 1
                
                if indegree[nei] == 0:
                    queue.append(nei)
                    
        return cnt == numCourses
    