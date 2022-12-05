# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        slow = head
        fast = head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        return slow if fast is None else slow.next
    