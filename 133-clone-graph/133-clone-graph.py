"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node
        
        nodes = dict()
        def build(head):
            if head.val not in nodes:
                nodes[head.val] = Node(head.val)
            else:
                return nodes[head.val]
            
            neigh = []
            for nei in head.neighbors:
                neigh.append(build(nei))
                
            nodes[head.val].neighbors = neigh
            return nodes[head.val]
        
        return build(node)
        
        
        
    '''
    def solve(self, node):
        if not node:
            return node
        
        d = defaultdict(list)
        q = deque([node])
        visited = set()
        
        while q:
            # print([i.val for i in q])
            node = q.popleft()
            
            for neighbor in node.neighbors:
                if neighbor.val not in d[node.val]:
                    d[node.val].append(neighbor.val)
                    
                if neighbor.val not in visited:
                    visited.add(neighbor.val)
                    q.append(neighbor)
                    
        if len(visited) <= 1:
            return Node(node.val)
        
        nodes = dict()
        
        for i in d:
            nodes[i] = Node(i)
            
        for k, v in d.items():
            for nei in v:
                nodes[k].neighbors.append(nodes[nei])
                
        return nodes[1] if 1 in nodes else []
        '''
    