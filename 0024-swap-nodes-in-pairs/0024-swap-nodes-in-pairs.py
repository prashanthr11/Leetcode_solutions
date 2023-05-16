# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ref = ListNode(0, head)
        ret = ref
        
        while head and head.next:
            present = head
            next_next = head.next.next
            
            ref.next = present.next
            ref = ref.next
            ref.next = present
            ref = ref.next
            present.next = next_next
            head = head.next
            
        return ret.next
    