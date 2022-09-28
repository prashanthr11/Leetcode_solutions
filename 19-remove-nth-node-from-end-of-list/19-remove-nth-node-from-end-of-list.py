# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        ln = self.recursive(head, n, 0)
        
        if ln == n:
            return head.next
        
        return head
        
    def recursive(self, head, n, ln):
        if not head:
            return ln
        
        length = self.recursive(head.next, n, ln + 1)
        
        if length - ln - 1 == n:
            head.next = head.next.next

        return length
        
    def solve(self, head, n):
        head = self.reverse(head)
        tmp = head
        
        if n != 1:
            while n - 1 != 1:
                tmp = tmp.next
                n -= 1

            tmp.next = tmp.next.next
        else:
            ref = head.next
            head.next = None
            head = ref
            
        return self.reverse(head)
    
    def reverse(self, head):
        prev = None
        while head:
            tmp = head.next
            head.next = prev
            prev = head
            head = tmp
            
        return prev