# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(root):
            prev = None
            while root:
                tmp = root.next
                root.next = prev
                prev = root
                root = tmp
                
            return prev
        
        l1 = reverse(l1)
        l2 = reverse(l2)
        
        ret = ListNode(0, None)
        ref = ret
        tmp = ref
        carry = 0
        
        while l1 or l2:
            if l1 and l2:
                value = l1.val + l2.val + carry
            elif l1:
                value = l1.val + carry
            else:
                value = l2.val + carry
                
            carry = value // 10
            value %= 10
            tmp.next = ListNode(value)
            tmp = tmp.next
            
            if l1:
                l1 = l1.next
                
            if l2:
                l2 = l2.next
                
        if carry:
            tmp.next = ListNode(carry)
            tmp = tmp.next

        return reverse(ref.next)
    