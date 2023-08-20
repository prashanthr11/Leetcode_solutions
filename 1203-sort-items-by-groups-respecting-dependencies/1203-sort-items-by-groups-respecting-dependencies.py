class Solution:
    def sortItems(self, n: int, m: int, group: List[int], beforeItems: List[List[int]]) -> List[int]:
        group_id = m
        
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1
                
        def topologicalsort(d, indegree):
            n = len(indegree)
            queue = deque([i for i in range(n) if indegree[i] == 0])
            visited = []
            
            while queue:
                top = queue.popleft()
                visited.append(top)
                
                for child in d[top]:
                    indegree[child] -= 1
                    
                    if indegree[child] == 0:
                        queue.append(child)
                        
            return visited if len(visited) == n else []
        
        item_indegree = [0] * n
        item_graph = defaultdict(list)
                
        group_indegree = [0] * group_id
        group_graph = defaultdict(list)
        
        for cur in range(n):
            for prior in beforeItems[cur]:
                item_graph[prior].append(cur)
                item_indegree[cur] += 1
                
                if group[prior] != group[cur]:
                    group_graph[group[prior]].append(group[cur])
                    group_indegree[group[cur]] += 1
                    
        items_order = topologicalsort(item_graph, item_indegree)
        groups_order = topologicalsort(group_graph, group_indegree)

        if not items_order or not groups_order:
            return []
        
        d = defaultdict(list)
        for item_order in items_order:
            d[group[item_order]].append(item_order)
        
        ret = []
        for order in groups_order:
            ret += d[order]
            
        return ret
    