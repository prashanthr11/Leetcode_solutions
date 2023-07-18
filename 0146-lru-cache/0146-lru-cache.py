from collections import OrderedDict as od

class LRUCache:

    def __init__(self, a: int):
        self.l = od()
        self.maxi = a

    def get(self, k: int) -> int:
        if k not in self.l:
            return -1
        self.l.move_to_end(k)
        return self.l[k]
            

    def put(self, k: int, v: int) -> None:
        self.l[k] = v
        self.l.move_to_end(k)

        if len(self.l) > self.maxi:
            self.l.popitem(last=False)


class DoubleLinkedList:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next
        
class LRUCacheTest:

    def __init__(self, a: int):
        self.d = {}
        self.last_element = None
        self.maxi = a
        self.head = None
        
    def get(self, k: int) -> int:
        if k not in self.d:
            return -1
        
        tmp = self.d[k]
        node = tmp
        
        if node.prev:
            if node.next:
                node.prev.next = node.next
            
        if node.next:
            node.next.prev = node.prev
            node.next.next = node
            node.prev = node.next
        
        node.next = None
        last_node = self.last_element
        if last_node != node:
            last_node.next = node
            node.prev = last_node
        
        self.last_element = node    
        return tmp.val

    def put(self, k: int, v: int) -> None:
        if k in self.d:
            self.d[k].val = v
            self.get(k)
            
        else:
            self.d[k] = DoubleLinkedList(v, self.last_element)
            
            if self.head is None:
                self.head = self.d[k]
            
            if self.last_element:
                last_node = self.last_element
                if last_node != self.d[k]:
                    last_node.next = self.d[k]
                    self.d[k].prev = last_node
                    
            self.last_element = self.d[k]
                
            if len(self.d) > self.maxi:
                self.head = self.head.next
                self.head.prev = None