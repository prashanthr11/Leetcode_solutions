# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        ret = head
        cnt = 0
        ref1 = head
        ref = head
        
        while head:
            cnt += 1
            if cnt == k:
                first = head.val
                ref1 = head
                
            if cnt - k > 0:
                ref = ref.next
            head = head.next
        
        ref1.val = ref.val
        ref.val = first
        return ret
    