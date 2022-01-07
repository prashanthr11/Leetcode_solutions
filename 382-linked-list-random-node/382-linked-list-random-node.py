# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        head = self.head
        ret = None
        scope = 1
        
        while head:
            if random.random() < 1/scope:
                ret = head.val
            head = head.next
            scope += 1
            
        return ret

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()