# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        first, second = ListNode(), ListNode()
        first_ref, second_ref = first, second
        
        while head:
            if head.val < x:
                first.next = head
                first = first.next
            else:
                second.next = head
                second = second.next
                
            head = head.next
            
        first.next = second_ref.next
        second.next = None
        return first_ref.next
    
        