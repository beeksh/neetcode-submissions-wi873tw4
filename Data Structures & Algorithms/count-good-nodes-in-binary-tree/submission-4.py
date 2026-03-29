# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        out = []
        def x(curr, m):
            if not curr:
                return
            if curr.val>=m:
                out.append(curr.val)
                m = curr.val
            x(curr.left, m)
            x(curr.right, m)
        x(root, root.val)
        return len(out)
