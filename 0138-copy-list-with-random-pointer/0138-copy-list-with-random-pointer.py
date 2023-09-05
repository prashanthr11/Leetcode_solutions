"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        ret = Node(0)
        ret_ref = ret
        dt = {}
        lst = []
        
        while head:
            node = Node(head.val)
            dt[head] = node
            if head.random:
                lst.append((node, head.random))
                
            ret.next = node
            ret = ret.next
            head = head.next
            
        for node, prev in lst:
            node.random = dt[prev]
            
        return ret_ref.next
    