# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        return self.optimise(head)
    
    
    def optimise(self, head):
        '''
        Time Complexity: O(N)
        Space Complexity: O(1)
        '''
        maxi = 0
        slow, fast = head, head.next
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        tmp = slow.next
        prev = None
        while tmp:
            nxt = tmp.next
            tmp.next = prev
            prev = tmp
            tmp = nxt
        slow.next = prev
        
        fast = slow.next
        while fast:
            maxi = max(maxi, fast.val + head.val)
            head = head.next
            fast = fast.next
            
        return maxi
    
    
    def naive(self, head):
        '''
        Time Complexity: O(N)
        Space Complexity: O(N)
        '''
        lst = []
        
        while head:
            lst.append(head.val)
            head = head.next
            
        i, ln = 0, len(lst)
        maxi = 0
        
        while i < ln // 2:
            maxi = max(maxi, lst[i] + lst[ln - 1 - i])
            i += 1
            
        return maxi
    