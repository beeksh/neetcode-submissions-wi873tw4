class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def match(l, r):
            if not l and not r:
                return True
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            return match(l.left, r.left) and match(l.right, r.right)

        def dfs(curr):
            if not curr:
                return False
            
            if match(curr, subRoot):
                return True
            
            return dfs(curr.left) or dfs(curr.right)

        return dfs(root)