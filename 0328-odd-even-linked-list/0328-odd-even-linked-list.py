# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        return self.method_2(head)
    
    def method_2(self, head):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        if not head or not head.next:
            return head
        
        odd = ListNode(-1)
        even = ListNode(-1)
        odd_ref = odd
        even_ref = even
        
        while head:
            odd.next = head
            odd = odd.next
            head = head.next
            
            if not head:
                break
                
            even.next = head
            even = even.next
            head = head.next
            
        odd.next = even_ref.next
        even.next = None
        
        return odd_ref.next
            
    def method_1(self, head):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        if not head or not head.next:
            return head
        
        odd = ListNode(-1)
        even = ListNode(-1)
        odd_ref = odd
        even_ref = even
        flag = 0
        
        while head:
            if flag == 0:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
                
            head = head.next
            flag ^= 1
            
        odd.next = even_ref.next
        even.next = None
        
        return odd_ref.next
    