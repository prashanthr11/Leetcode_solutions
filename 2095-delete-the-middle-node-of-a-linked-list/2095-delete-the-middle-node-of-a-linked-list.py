# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        slow, fast = head, head
        prev = None
        
        while fast and fast.next:
            fast = fast.next.next
            prev = slow
            slow = slow.next
            
        if prev:
            prev.next = slow.next
        else:
            head = None
            
        return head
    