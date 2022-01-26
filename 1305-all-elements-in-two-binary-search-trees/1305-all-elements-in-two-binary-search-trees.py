# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        l = []
        def solve(root1, root2):
            q = deque([root1, root2])

            while q:
                top = q.popleft()

                if top is None:
                    continue

                # l.append(top.val)
                yield top.val
                if top.left:
                    q.append(top.left)

                if top.right:
                    q.append(top.right)

        return sorted(solve(root1, root2))
    