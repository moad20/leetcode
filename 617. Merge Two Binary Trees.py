class Solution:
    def mergeTrees(self, r1: Optional[TreeNode], r2: Optional[TreeNode]) -> Optional[TreeNode]:
        match (r1, r2):
            case (None, None): return None
            case (None, r) | (r, None): return r
            case _: 
                r1.val += r2.val
                r1.left = self.mergeTrees(r1.left, r2.left) 
                r1.right = self.mergeTrees(r1.right, r2.right) 
                return r1