class ListNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = self.next = None
        

class LRUCache:

    def __init__(self, capacity: int):
        self.maxi = capacity
        self.cache = {}
        self.left_most, self.right_most = ListNode(0, 0), ListNode(0, 0)
        self.left_most.next = self.right_most
        self.right_most.prev = self.left_most

    
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        self.remove(self.cache[key])
        self.add(self.cache[key])
        return self.cache[key].val
    

    def put(self, key: int, value: int) -> None:
        if key in self.cache:            
            self.remove(self.cache[key])
            
        self.cache[key] = ListNode(key, value)
        self.add(self.cache[key])
        
        if len(self.cache) > self.maxi:
            del self.cache[self.left_most.next.key]
            self.remove(self.left_most.next)
            
    def remove(self, node):
        left, right = node.prev, node.next
        left.next = right
        right.prev = left
        
    def add(self, node):
        left = self.right_most.prev
        left.next = self.right_most.prev = node
        node.prev = left
        node.next = self.right_most

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)