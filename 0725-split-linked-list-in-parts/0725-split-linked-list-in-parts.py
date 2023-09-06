# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        def get_len(tmp):
            cnt = 0
            while tmp:
                tmp = tmp.next
                cnt += 1
            return cnt
        
        ln = get_len(head)
        ret = []

        div, mod = divmod(ln, k)
        prev = None
        while head:
            if prev:
                prev.next = None

            ret.append(head)
            for i in range(div):
                prev = head
                head = head.next

            if mod:
                prev = head
                head = head.next
                mod -= 1
                
        if k - ln > 0:
            ret += [None for _ in range(k - ln)]

        return ret
