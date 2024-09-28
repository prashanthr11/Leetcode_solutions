"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        if not node:
            return None
        
        mappings = defaultdict(list)
        
        def fill_neighbours(node):
            nonlocal mappings
            
            for child in node.neighbors:
                if child.val not in mappings[node.val]:
                    mappings[node.val].append(child.val)
                    fill_neighbours(child)
                
        fill_neighbours(node)
        
        new_nodes = {}
        
        for i in mappings:
            new_nodes[i] = Node(i)
            
        for k, v in mappings.items():
            new_nodes[k].neighbors = [new_nodes[i] for i in v]
            
        return new_nodes.get(1, Node(1))
    