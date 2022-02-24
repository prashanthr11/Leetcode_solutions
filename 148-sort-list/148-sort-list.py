# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.naive(head)
        
    def naive(self, head):
        '''
        Time Complexity: O(N Log N)
        Space Complexity: O(N)
        '''
        lst = []
        while head:
            lst.append(head.val)
            head = head.next
            
        ret = ListNode()
        ret_ptr = ret
        for i in sorted(lst):
            ret.next = ListNode(i)
            ret = ret.next
            
        return ret_ptr.next
    