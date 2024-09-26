# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        lst = self.get_elements(head)
        return self.build_balanced_bst(lst, 0, len(lst) - 1)
    
    def build_balanced_bst(self, lst, low, high):
        if low > high:
            return None
        
        mid = low + (high - low) // 2
        if (high - low) % 2 != 0:
            mid = mid + 1
        
        node = TreeNode(lst[mid])
        node.left = self.build_balanced_bst(lst, low, mid - 1)
        node.right = self.build_balanced_bst(lst, mid + 1, high)
        
        return node
        
        
    def get_elements(self, head):
        ret = []
        
        while head:
            ret.append(head.val)
            head = head.next
            
        return ret
    