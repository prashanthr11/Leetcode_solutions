# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        cur = root
        stk = []
        ret = []

        while cur or stk:
            while cur:
                stk.append(cur)
                cur  = cur.left

            left_most_node = stk.pop()
            ret.append(left_most_node.val)
            cur = left_most_node.right

        return ret
    