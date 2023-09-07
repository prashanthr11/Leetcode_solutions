# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if left == right:
            return head
        
        prev = ListNode(0, head)
        prev_ref = prev
        for i in range(left - 1):
            prev = prev.next
            head = head.next
        
        cur = head
        cur_ref = cur
        tmp = cur.next
        
        for i in range(right - left):
            res = tmp.next
            tmp.next = cur
            cur = tmp
            tmp = res
            
        cur_ref.next = res
        prev.next = cur
        
        return prev_ref.next
        