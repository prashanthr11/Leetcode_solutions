class Solution:
    def mergeKLists(self, lists):
        return self.optimise(lists)
    
    def optimise(self, lists):
        '''
        Time Complexity: O(N LogM)
        Space Complexity: O(1)
        '''
        ln = len(lists)
        
        if ln == 0:
            return None
        
        if ln == 1:
            return lists[0]
        
        while ln > 1:
            pos = 0
            if ln % 2:
                for i in range(0, ln - 1, 2):
                    lists[pos] = self.merge(lists[i], lists[i + 1])
                    pos += 1
                    
                lists[pos] = lists[ln - 1]
                ln = ln // 2 + 1
            else:
                for i in range(0, ln, 2):
                    lists[pos] = self.merge(lists[i], lists[i + 1])
                    pos += 1
                    
                ln //= 2
                
        return lists[0]
    
    def naive(self, lists):
        '''
        Time Complexity: O(N*M) where N is the length of the given List and M is the length of the linkedlist in the list.
        Space Complexity: O(1)
        '''
        ln = len(lists)
        
        if not ln:
            return None
        
        head = None
        
        for i in range(ln):
            head = self.merge(head, lists[i])
            
        return head
    
    def merge(self, head1, head2):
        '''
        Time Complexity: O(N + M) where N and M are lengths of head1 and head2 respectively
        Space Complexity: O(1)
        '''
        ret = ListNode()
        ret_ptr = ret
        
        while head1 or head2:
            if head1 is None:
                ret.next = head2
                break
            
            if head2 is None:
                ret.next = head1
                break
            
            if head1.val < head2.val:
                ret.next = head1
                head1 = head1.next
            else:
                ret.next = head2
                head2 = head2.next
                
            ret = ret.next
            
        return ret_ptr.next
    