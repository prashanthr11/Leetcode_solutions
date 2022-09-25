class Node:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class MyCircularQueue:

    def __init__(self, k: int):
        self.root = None
        self.k = k
        self.cnt = 0
        
    def enQueue(self, value: int) -> bool:
        if self.cnt + 1 > self.k:
            return False
        
        if not self.root:
            new_node = Node(value)
            self.root = new_node
            self.root.prev = self.root.next = new_node
        else:
            tmp_root, tmp_cnt = self.root, self.cnt
            
            while tmp_cnt - 1 > 0 and tmp_root.next:
                tmp_root = tmp_root.next
                tmp_cnt -= 1
                
            tmp_root.next = Node(value, tmp_root, self.root)
            self.root.prev = tmp_root.next
        
        self.cnt += 1            
        return True

    def deQueue(self) -> bool:
        if not self.cnt:
            return False
        
        tmp_root = self.root
        
        if tmp_root == tmp_root.next:
            self.root = None
        else:
            self.root = tmp_root.next
            self.root.prev = tmp_root.prev
            tmp_root.prev.next = self.root
            
        self.cnt -= 1
        return True

    def Front(self) -> int:
        return self.root.val if self.cnt else -1

    def Rear(self) -> int:
        return self.root.prev.val if self.cnt else -1

    def isEmpty(self) -> bool:
        return self.cnt == 0

    def isFull(self) -> bool:
        return self.cnt == self.k
        


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()