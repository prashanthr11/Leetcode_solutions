# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        def solve(head):
            if not head:
                return head

            if not head.next:
                return head

            prev = head
            head = head.next
            head_ref = head

            while head:
                tmp = head.next
                head.next = prev
                if tmp:
                    head = tmp.next
                else:
                    head = tmp

                if head:
                    prev.next = head
                else:
                    prev.next = tmp

                prev = tmp

            return head_ref
        return solve(head)