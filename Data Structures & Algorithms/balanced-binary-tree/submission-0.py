# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.state = True

        def dfs(curr):
            if not curr:
                return 0

            l = dfs(curr.left)
            r = dfs(curr.right)
            if abs(l-r)>1:
                self.state = False
            return 1+max(l,r)
        
        dfs(root)

        return self.state